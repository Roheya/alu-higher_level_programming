#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            except (ValueError, TypeError):
                # Skip silently if not an integer
                continue
        print()  # new line after printing
        return count
    except IndexError:
        # If x is bigger than the length of my_list, IndexError will occur
        raise
