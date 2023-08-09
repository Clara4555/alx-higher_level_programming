#!/usr/bin/python3  
for ascii_char in range(ord('a'), ord('z') + 1):
    if ascii_char != ord('q') and ascii_char != ord('e'):   
        print("{}".format(chr(ascii_char)), end="")
