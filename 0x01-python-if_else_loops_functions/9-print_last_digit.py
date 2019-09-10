#!/usr/bin/python3
def print_last_digit(number):
    Last = abs(number) % 10
    print("{:d}".format(Last), end='')
    return (Last)
