#!/usr/bin/python3
def weight_average(my_list=[]):
    the_sum = 0
    w_sum = 0
    if not my_list:
        return (0)
    for score, weight in my_list:
        the_sum += score * weight
        w_sum += weight
    the_av = the_sum / w_sum
    return (the_av)
