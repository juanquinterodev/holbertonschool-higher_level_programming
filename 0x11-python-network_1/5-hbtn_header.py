#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id
in the response header"""
from requests import get
from sys import argv


if __name__ == '__main__':
    url = get(argv[1])
    print(url.headers.get('X-Request-Id'))
