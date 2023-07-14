#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    num = len(argv)
    n = argv[0]
    if num != 4:
        print("Usage: {} <a> <operator> <b>".format(n))
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    oper = argv[2].lower()
    if oper == '+':
        print("{} {} {} = {}".format(a, oper, b, add(a, b)))
    elif oper == '-':
        print("{} {} {} = {}".format(a, oper, b, sub(a, b)))
    elif oper == '*':
        print("{} {} {} = {}".format(a, oper, b, mul(a, b)))
    elif oper == '/':
        print("{} {} {} = {}".format(a, oper, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
