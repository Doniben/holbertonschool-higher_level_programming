#!/usr/bin/python3


def number_of_lines(filename=""):
    with open(filename, encoding="UTF-8") as F:
        size = 0
        for line in F:
            size + size + 1
        return size
