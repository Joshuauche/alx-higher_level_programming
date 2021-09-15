#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    mynew_list = list(uniq_list)
    return sum(mynew_list)
