""" An algorithm such that if an element in an MxN matrix is 0, its entire row and
    column is set to 0
    Time complexity O(n^2)
    Space Complexity O(n)"""

import numpy

M = 5
N = 5
A = numpy.random.random_integers(0, 10, (M, N))
rows = dict()
columns = dict()


def answer(A):
    for i in range(M):
        for j in range(N):
            if A[i][j] == 0:
                rows[i] = 1
                columns[j] = 1
                continue

    for i in range(M):
        for j in range(N):
            if i in rows or j in columns:
                A[i][j] = 0


print A
answer(A)
print A
