#!/usr/bin/env python3
import json


def sort_dict_file(file_name: str):
    print('Sorting', file_name)

    with open(file_name, 'r') as f:
        dictionary = json.load(f)

    dictionary['words'] = list(set(dictionary['words']))
    dictionary['words'].sort()

    with open(file_name, 'w') as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    with open('./catalog.json', 'r') as cf:
        catalog = json.load(cf)

    for lang_dicts in catalog['dictionaries'].values():
        for dict_file in lang_dicts:
            sort_dict_file(dict_file)
