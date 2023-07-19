#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    my_list2 = list(set(my_list))
    for i in range(0, len(my_list2)):
        result += my_list2[i]
    return (result)
