#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        temp = list(my_list)
        return temp
    elif idx > len(my_list) - 1:
        temp = list(my_list)
        return temp
    else:
        temp = list(my_list)
        my_list[idx] = element
        return temp
