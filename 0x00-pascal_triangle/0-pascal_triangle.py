#!/usr/bin/python3
"""
pascal triangle
"""
def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the given number of rows.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.

    Raises:
        None.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) < n:
        prev_row = triangle[-1]
        new_row = [1]

        for i in range(len(prev_row) - 1):
            new_row.append(prev_row[i] + prev_row[i + 1])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
