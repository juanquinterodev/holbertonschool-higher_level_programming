#!/usr/bin/python3
class MyInt(int):

    def __init__(self, value):
        self.value = value
        int.__init__(self)

    def __eq__(self, x):
        return self.value != x

    def __neg__(self, x):
        return self.value == x
