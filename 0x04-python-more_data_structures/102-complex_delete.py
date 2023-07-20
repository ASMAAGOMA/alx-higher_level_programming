#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    deleted_key = []
    if not value:
        return (a_dictionary)
    for key, v in a_dictionary.items():
        if v == value:
            deleted_key.append(key)
    for key in deleted_key:
        del a_dictionary[key]
    return (a_dictionary)
