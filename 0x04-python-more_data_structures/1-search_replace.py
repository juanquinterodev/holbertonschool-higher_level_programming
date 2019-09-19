#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for i in my_list:
        if i != search:
            new.append(i)
        else:
            new.append(replace)
    return new
