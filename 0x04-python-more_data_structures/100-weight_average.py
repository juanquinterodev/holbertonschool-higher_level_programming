#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    x = sum([i * j for i, j in my_list])
    y = sum([j for i, j in my_list])
    if not y:
        return 0
    return x/y
