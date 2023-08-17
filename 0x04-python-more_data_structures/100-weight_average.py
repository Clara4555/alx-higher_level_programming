#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    int_num = 0
    den = 0
    for x in my_list:
        int_num += x[0] * x[1]
        den += x[1]
    return (int_num / den)
