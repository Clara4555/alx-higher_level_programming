#!/usr/bin/python3
def number_keys(a_dictionary):
    keys = 0
    dict_keys = list(a_dictionary.keys())
    for a in dict_keys:
        keys += 1
    return (keys)
