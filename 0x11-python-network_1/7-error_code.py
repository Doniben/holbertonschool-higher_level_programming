#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and
displays the body of the response. """

import requests
from requests.exceptions import HTTPError
import sys

if __name__ == "__main__":
    try:
        arg = requests.get(sys.argv[1])
        arg.raise_for_status()
        print(arg.text)
    except HTTPError as err:
        print("Error code: {}".format(err.response.status_code))
