#!/usr/bin/python3
if __name__ == "__main__":
    import importlib
    from add_0 import add
    a = 1
    b = 2
    result = add(a, b)
    print("{} + {} ={}".format(a, b, result))