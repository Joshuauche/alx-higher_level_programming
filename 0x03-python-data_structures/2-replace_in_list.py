#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in my_list:
        if idx < 0:
            print("{:d}".format(i))
        elif idx > len(my_list):
            print("{:d}".format(i))
        else:
            my_list[idx] = element
            return my_list
