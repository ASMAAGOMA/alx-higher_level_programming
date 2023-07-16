#!/usr/bin/env python3
def no_c(my_string):
    char_list = list(my_string)
    for i, char in enumerate(char_list):
        if char_list[i] == 'c' or char_list[i] == 'C':
            char_list[i] = ''
        else:
            continue
    new_string = ''.join(char_list)
    return (new_string)
