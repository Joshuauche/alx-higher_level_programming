#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            result += chr(ord(char) - 32)
        else:
            result = char
            print("{:s}".format(result), end="")
            print('')
