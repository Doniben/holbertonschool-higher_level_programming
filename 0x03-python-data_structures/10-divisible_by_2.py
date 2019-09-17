#!/usr/bin/python3
def divisible_by_2(my_list=[]):
        if len(my_list) == 0:
                return None
        new_str = []
        for i in my_list:
                if i % 2 == 0:
                        new_str.append(True)
                else:
                        new_str.append(False)
        return new_str
