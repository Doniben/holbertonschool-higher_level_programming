#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    counter = 0
    with open(filename, encoding="utf-8") as F:
        for line in F:
            counter += 1
            if nb_lines <= 0 or nb_lines >= counter:
                print(line, end='')
