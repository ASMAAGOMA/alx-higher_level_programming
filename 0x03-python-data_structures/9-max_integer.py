#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)
    least_num = my_list[0]
    for i in my_list:
        if i > least_num:
            least_num = i
            return (least_num)
