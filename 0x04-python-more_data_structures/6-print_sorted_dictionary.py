#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_k = sorted(a_dictionary.keys())
    for k in sorted_k:
        v = a_dictionary[k]
        print(f"{k}: {v}")
