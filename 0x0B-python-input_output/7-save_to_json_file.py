#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    with open(filename, encoding="utf-8", "w") as F:
        F.write(json.dumbs(my_obj))
