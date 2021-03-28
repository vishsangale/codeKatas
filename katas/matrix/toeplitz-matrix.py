"""
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
"""
from typing import List


def is_toeplitz(matrix: List[List[int]]) -> int:
    nr_rows = len(matrix)
    nr_cols = len(matrix[0])

    if nr_rows == 0 or nr_cols == 0:
        return True

    for col in range(nr_cols):
        col_idx = 0
        item = matrix[0][col]
        for row in range(nr_rows):
            col_idx = col + row
            if col_idx < nr_cols:
                if item != matrix[row][col_idx]:
                    return False

    for row in range(nr_rows):
        row_idx = 0
        item = matrix[row][0]
        for col in range(nr_cols):
            row_idx = row + col
            if row_idx < nr_rows:
                if item != matrix[row_idx][col]:
                    return False

    return True


def test_is_toeplitz():

    m = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    assert is_toeplitz(m)

    assert is_toeplitz([[]])
    assert is_toeplitz([[1, 2, 3]])
    assert is_toeplitz([[1, 2, 3], [5, 1, 2]])

    assert not is_toeplitz([[1, 2, 3], [5, 2, 1]])
    assert not is_toeplitz([[1, 2, 3], [5, 1, 2], [9, 1, 1]])
