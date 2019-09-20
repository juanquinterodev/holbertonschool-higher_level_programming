#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        mult = a_dictionary.copy()
        for i in a_dictionary:
            mult[i] = a_dictionary[i] * 2
        return mult
