#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    update = {}
    for value in a_dictionary:
        update[value] = a_dictionary[value] * 2
    return update
