""" Implementation of Quick sort algorithm using Lomuto partition scheme
    Time complexity worst O(n^2) average case O(n*log(n))
    Space complexity O(1)
    """
import random


def partition(A, start, end):
    pivot = A[end]
    part_index = start
    for i in range(start, end + 1):
        if A[i] < pivot:
            temp = A[i]
            A[i] = A[part_index]
            A[part_index] = temp
            part_index += 1
    temp = A[part_index]
    A[part_index] = A[end]
    A[end] = temp
    return part_index


def quick_sort(A, start, end):
    if start < end:
        index = partition(A, start, end)
        quick_sort(A, start, index - 1)
        quick_sort(A, index + 1, end)


A = random.sample(range(1, 10), 5)
print A
quick_sort(A, 0, len(A) - 1)
print A
