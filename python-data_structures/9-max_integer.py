#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:   # if the list is empty
        return None

    max_val = my_list[0]   # start with the first element
    for num in my_list[1:]:
        if num > max_val:
            max_val = num
    return max_val
