#!/usr/bin/python3
def no_c(my_string):
    new = my_string.translate({67: None, 99: None})
    return new
