#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    a = 0

    for i in sys.argv:
        if i != sys.argv[0]:
            a = int(i) + a
    print(a)
