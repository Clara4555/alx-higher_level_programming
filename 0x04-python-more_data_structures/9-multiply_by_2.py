#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mul = a_dictionary.copy()
    listt = list(mul.keys())
    for a in listt:
        mul[a] *= 2
    return (mul)
