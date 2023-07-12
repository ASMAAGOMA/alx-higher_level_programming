#!/usr/bin/python3
def print_last_digit(number):
    abs_number = abs(number)
    last_d = abs_number % 10
    print("{}".format(last_d), end="")
    return (last_d)
