#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and
displays the body of the response. """

from requests.exceptions import HTTPError
import requests
import sys

if __name__ == "__main__":
    try:
        arg = requests.get(sys.argv[1])
        arg.raise_for_status()
        print(arg.text)
    except requests.exceptions.HTTPError as err:
        print("Error code: {}".format(err.code))
