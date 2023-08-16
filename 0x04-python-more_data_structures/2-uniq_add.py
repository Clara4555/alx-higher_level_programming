#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = set(my_list)
    integer_num = 0
    for a in unique_integers:
        integer_num += a
    return(unique_integers)
