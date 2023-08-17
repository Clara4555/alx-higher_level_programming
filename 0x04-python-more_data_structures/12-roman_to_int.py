#!/usr/bin/python3
def to_subtract(list_num):
    total_sub = 0
    max_list = max(list_num)
    for b in list_num:
        if max_list > b:
            total_sub += b
    return (max_list - total_sub)
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(roman.keys())
    num = 0
    last_rom = 0
    list_num = [0]
    for x in roman_string:
        for r_num in list_keys:
            if r_num == x:
                if roman.get(x) <= last_rom:
                    num += to_subtract(list_num)
                    list_num = [roman.get(x)]
                else:
                    list_num.append(roman.get(x))
                last_rom = roman.get(x)
    num += to_subtract(list_num)
    return (num)
