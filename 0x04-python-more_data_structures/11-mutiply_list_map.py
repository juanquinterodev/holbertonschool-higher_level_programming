#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    return calc(map(lambda x: x*number, my_list)) if my_list is not None else None
