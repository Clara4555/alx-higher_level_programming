#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_newlist = []
    for a in range(0, list_length):
        try:
            division = my_list_1[a] / my_list_2[a]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            my_newlist.append(division)
    return (my_newlist)
