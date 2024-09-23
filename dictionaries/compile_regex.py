#!/usr/bin/env python3
import json
import re

with open('catalog.json', 'r') as f:
    catalog = json.load(f)

with open('replacements.json', 'r') as f:
    replacements = json.load(f)

with open('excludes.json', 'r') as f:
    excludes = json.load(f)

    for key, val in excludes.items():
        excludes[key] = re.compile('|'.join(val))

full_dicts = {}

for lang in catalog['languages']:
    words = set()
    for dict_fn in catalog['dictionaries'].get(lang, ()):
        with open(dict_fn, 'r') as f:
            dict_content = json.load(f)
        for word in dict_content['words']:
            words.add(word)
    full_dicts[lang] = words


def special_replacement(lang, id):
    rs = set(replacements.get('all', {}).get(id, ())) | set(
        replacements.get(lang, {}).get(id, ()))
    if not len(rs):
        return ''
    return f'(?:{"|".join(rs)})'


def check_exclude(key, word):
    if key in excludes:
        return not not excludes[key].search(word)

    return False


def word_with_replacements(lang, srcLang):
    exclKey = f'{srcLang}-{lang}'
    lang_replacements = dict(replacements.get(lang, []))
    for key, val in (replacements.get('all') or {}).items():
        lang_replacements[key] = set(lang_replacements.get(key, [])) | set(val)

    def transform(word):
        if check_exclude(exclKey, word):
            return ''
        s = ''
        for c in word:
            r = lang_replacements.get(c.lower(), None)
            if not r:
                s += c
            else:
                s += f'(?:{c}|{"|".join(r)})'
        return s
    return transform


written_regexps = []


def write_out_regexp(lang, exp):
    with open(f'regex/{lang}.json', 'w') as f:
        json.dump(exp, f, ensure_ascii=False)

    written_regexps.append(lang)


def write_out_regexp_index():
    with open('regex/index.js', 'w') as f:
        print('module.exports = {', file=f)

        for lang in written_regexps:
            print(
                f'  get ["{lang}"]() {{', file=f)
            print(
                f'    return new RegExp(require("./{lang}.json"), "gi");', file=f)
            print(
                f'  }},', file=f)

        print('};', file=f)


# Language specific expressions. Work when text language is known. Use more replacement variants
for lang, full_dict in full_dicts.items():
    if lang != 'all':
        if not len(full_dict):
            print('Empty dictionary for', lang)
            write_out_regexp(lang, '$.+^')  # this will match nothing
        else:
            begin = special_replacement(lang, "$begin")
            words_expressions = "|".join(
                filter(len, map(word_with_replacements(lang, lang), full_dict))
            )
            end = special_replacement(lang, "$end")
            write_out_regexp(lang, f'{begin}(?:{words_expressions}){end}')

# Common expressions. Used for texts in unknown languages.
all_res = []

for lang, full_dict in full_dicts.items():
    if not len(full_dict):
        continue
    begin = special_replacement(lang, '$begin')
    end = special_replacement(lang, '$end')
    words_expressions = "|".join(
        filter(len, map(word_with_replacements('all', lang), full_dict))
    )
    all_res.append(f'(?:{begin}(?:{words_expressions}){end})')

write_out_regexp('all', '|'.join(all_res))

write_out_regexp_index()
