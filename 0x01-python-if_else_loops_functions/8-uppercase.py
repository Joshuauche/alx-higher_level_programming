#!/usr/bin/python3
def uppercase(str):
    for char in str:
        result = ord(char)
        if result >= ord('a') and result <= ord('z'):
            rusult = result - 32
        print("{:c}".format(result), end="")
    print()
