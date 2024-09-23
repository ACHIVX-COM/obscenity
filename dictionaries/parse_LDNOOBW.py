#!/usr/bin/env python3
import json
import os


def read_out_words(lang):
    try:
        with open(os.path.join('LDNOOBW', lang), 'r') as f:
            s = str(f.read())
            return list(filter(len, s.split('\n')))
    except IOError as e:
        print('LDNOOBW does not provide', lang)
        return []


if __name__ == '__main__':
    with open('catalog.json', 'r') as f:
        catalog = json.load(f)

    dict_list = catalog['dictionaries']

    for k in dict_list.keys():
        dict_list[k] = filter(
            lambda x: not x.endswith('-LDNOOBW.json'),
            dict_list[k] or []
        )

    for lang in catalog['languages']:
        words = read_out_words(lang)
        if len(words) > 0:
          obj = {'language': lang, 'words': words}
          fn = 'parsed/{0}-LDNOOBW.json'.format(lang)
          with open(fn, 'w') as f:
              json.dump(obj, f)
              f.write('\n')
          dict_list[lang] = dict_list.get(lang, [])
          dict_list[lang].append(fn)

    with open('catalog.json', 'w') as f:
        json.dump(catalog, f, indent=2, sort_keys=True, separators=(',', ': '))
        f.write('\n')
