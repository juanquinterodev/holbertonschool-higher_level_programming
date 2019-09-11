#!/usr/bin/python3
def remove_char_at(str, n):
    x = 0
    c = ""
    for ch in str:
        if x != n:
            c = c + ch
        x += 1
    return (c)
