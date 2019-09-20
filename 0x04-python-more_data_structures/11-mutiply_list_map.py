#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    return None if my_list is None else mult(map(lambda x: x*number, my_list))
