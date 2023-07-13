#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_num = len(sys.argv) - 1
    if arg_num == 0:
        print("0 arguments.")
    else:
        print(f"{arg_num} argument{'s' if arg_num > 1 else ''}:")
        for i in range(1, arg_num + 1):
            print(f"{i}: {sys.argv[i]}")
