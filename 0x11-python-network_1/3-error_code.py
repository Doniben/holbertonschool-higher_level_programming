#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8). """

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    arg = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(arg) as response:
            print(response.read().decode())

    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
