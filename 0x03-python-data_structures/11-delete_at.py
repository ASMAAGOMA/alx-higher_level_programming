#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for i in my_list:
        if i == idx:
            del my_list[i]
    return (my_list)
