""" Matrix rotation by 90 degree to right
    Time complexity O(n^2)
    Space complexity O(1)"""

import numpy

N = 5

A = numpy.random.random_integers(0, 100, (N, N))

B = numpy.random.random_integers(0, 0, (N, N))


def transpose(A):
    for i in range(N):
        for j in range(i + 1, N):
            temp = A[i][j]
            A[i][j] = A[j][i]
            A[j][i] = temp


def reverse_rows(A):
    for i in range(N):
        for j in range(N / 2):
            temp = A[i][j]
            A[i][j] = A[i][N - 1 - j]
            A[i][N - 1 - j] = temp


def rotate(A):
    for i in range(N):
        for j in range(N):
            B[i][j] = A[N - j - 1][i]


print A
transpose(A)
reverse_rows(A)
print A
