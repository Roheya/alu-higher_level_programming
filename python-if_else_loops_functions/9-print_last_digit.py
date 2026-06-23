#!/usr/bin/env python3
def uppercase(str):
    """Prints a string in uppercase followed by a new line."""
    result = ""
    for ch in str:
        # Convert lowercase letters to uppercase using ASCII math
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        else:
            result += ch
    # First print: show the result
    print("{}".format(result))
    # Second print: just a newline (still uses string format)
    print("{}".format(""))
