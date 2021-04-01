"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

"""


def find_kth_positive(arr, k):
    missed_k = 1
    for i in range(1, arr[-1] + 1):
        if i not in arr:
            if missed_k == k:
                return i
            missed_k += 1
    return arr[-1] + (k - missed_k + 1)

def test_find_kth_positive():
    assert 9 == find_kth_positive([2, 3, 4, 7, 11], 5)

    assert 6 == find_kth_positive([1,2,3,4], 2)
