#!/usr/bin/python3
"""
Function that returns Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        # Each new row starts and ends with 1
        row = [1]
        # Fill in the middle values
        for j in range(1, len(prev_row)):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
