#!/usr/bin/python3
"""sends a request to the URL and displays the body
of the response (decoded in utf-8)"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == '__main__':
    req = Request(argv[1])
    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as status:
        print('Error code: {}'.format(status.code))
