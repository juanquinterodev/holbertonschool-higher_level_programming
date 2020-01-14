#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id variabler"""
from urllib import request
from sys import argv


if __name__ == '__main__':
    with request.urlopen(argv[1]) as response:
        req = response.info()

    print(req['X-Request-Id'])
