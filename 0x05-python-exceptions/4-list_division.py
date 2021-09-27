#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for index in range(0, list_length):
        try:
            check = (my_list_1[index] / my_list_2[index])
        except TypeError:
            check = 0
            print("wrong type")
        except ZeroDivisionError:
            check = 0
            print("division by 0")
        except IndexError:
            check = 0
            print("out of range")
        finally:
            pass
        result.append(check)
    return result
