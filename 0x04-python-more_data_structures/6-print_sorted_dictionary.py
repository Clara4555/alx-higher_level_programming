#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_order = list(a_dictionary.keys())
    sort_order.sort()
    for a in sort_order:
        print("{}: {}".format(a, a_dictionary.get(a)))
