#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    if idx < 0 or idx > len(my_list) - 1:
        return (my_list)
    for i in my_list:
        if i == idx:
            del my_list[i]
            new_list = my_list
    return (new_list)
