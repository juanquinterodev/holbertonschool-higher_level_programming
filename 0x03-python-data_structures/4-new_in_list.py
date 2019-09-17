#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lista = []
    lista = list(my_list)
    if idx < 0:
        return(lista)
    elif idx >= len(my_list):
        return(lista)
    else:
        lista[idx] = element
        return(lista)
