#!/usr/bin/python3
""" Python script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8) """

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":

    url = (sys.argv[1])
    email = {"email": (sys.argv[2])}

    data = urllib.parse.urlencode(email).encode()
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode())
