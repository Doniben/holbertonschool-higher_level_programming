#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):

    n_list = []
    div = 0

    for i in range(list_length):
        try:
            div = my_list_1 / my_list_2
        except ZeroDivisionError:
            print("division by 0")
        except (ValueError, TypeError):
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            n_list.append(div)
        div = 0
    return n_list
