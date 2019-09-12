#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = 1
    if len(sys.argv) == 2:
        print((len(sys.argv) - 1), "argument:")
    elif len(sys.argv) > 2:
        print((len(sys.argv) - 1), "arguments:")
    else:
        print((len(sys.argv) - 1), "arguments.")
    for i in sys.argv:
        if i != sys.argv[0]:
            print("{}: {}".format(a, i))
            a = a + 1
