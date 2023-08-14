#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiples_list = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            multiples_list.append(True)
        else:
            multiples_list.append(False)
    return (multiples_list)
