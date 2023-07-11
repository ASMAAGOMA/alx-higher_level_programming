#!/usr/bin/python3
for l_alpha in range(97, 123):
    alpha = chr(l_alpha)
    if alpha not in ['e', 'q']:
        print("{}".format(alpha), end="")
