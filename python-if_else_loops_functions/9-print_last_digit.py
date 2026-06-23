#!/usr/bin/env python3
def uppercase(str):
    """Prints a string in uppercase followed by a new line."""
    result = ""
    for ch in str:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        else:
            result += ch
    print("{}".format(result))
