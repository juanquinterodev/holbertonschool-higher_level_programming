#!/usr/bin/python3
"""takes your Github credentials and uses 
the Github API to display your id"""
from requests import get
from sys import argv


if __name__ == '__main__':
    url = get('https://api.github.com/user', auth=(argv[1], argv[2]))
    val = url.json()
    print(val.get('id'))
