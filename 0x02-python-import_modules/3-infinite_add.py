#!/usr/bin/python3
def add(argv):
    num = len(argv) - 1
    if num == 0:
        print("{}".format(num))
        return
    else:
        i = 1
        adding = 0
        while i <= num:
            adding += int(argv[i])
            i += 1
        print("{}".format(adding))


if __name__ == "__main__":
    import sys
    add(sys.argv)
