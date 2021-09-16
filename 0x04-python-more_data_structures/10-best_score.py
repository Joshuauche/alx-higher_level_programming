#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        max_num = 0
        for key, value in a_dictionary.items():
            if value > max_num:
                max_num = value
        for key, value in a_dictionary.items():
            if value == max_num:
                return key
