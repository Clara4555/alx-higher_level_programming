#!/usr/bin/python3
for print_number in range(0, 100):
    if print_number == 99:
        print("{}".format(print_number))
    else:
        print("{:02}".format(print_number), end=",")
