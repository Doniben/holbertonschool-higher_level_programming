#!/usr/bin/python3
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

n_list = []

try:
    n_list = list(load_from_json_file("add_item.json"))

except:
    len(n_list) == 0

for args in range(1, len(argv)):
    n_list.append(argv[args])

save_to_json_file(n_list, "add_item.json")
