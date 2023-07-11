#!/usr/bin/python3
i = 0
for i in range(99):
    hex_i = hex(i)
    print("{:01d} = {}".format(i, hex_i))
    i += 1
