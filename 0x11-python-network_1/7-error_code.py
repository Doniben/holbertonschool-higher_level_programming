#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and
displays the body of the response. """

from requests.exceptions import HTTPError
import requests
import sys

if __name__ == "__main__":
    try:
        arg = requests.get(sys.argv[1])
        print(arg.text)
    except HTTPError as err
        print("Error code: {}".format(err))
