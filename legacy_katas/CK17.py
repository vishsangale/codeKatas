""" Given an arrayOfInts, find the highestProduct you can get from three of the integers."""
import random

import sys
from numpy import inf


def solution1(a):
    n = len(a)
    if n < 3:
        raise Exception("Array is smaller than 3")
    p = a[0] * a[1] * a[2]

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                p = max(p, a[i] * a[j] * a[k])
    return p


def solution2(a):
    n = len(a)
    if n < 3:
        raise Exception("Array is smaller than 3")
    a.sort()
    m1 = a[-1] * a[-2] * a[-3]
    m2 = a[0] * a[1] * a[-1]
    return max(m1, m2)


def solution3(a):
    n = len(a)
    if n < 3:
        raise Exception("Array is smaller than 3")
    mn1 = mn2 = max(a)
    mx1 = mx2 = mx3 = min(a)
    for i in range(n):
        m = max(mn1, mn2)
        if m > a[i]:
            if m == mn1:
                mn1 = a[i]
            else:
                mn2 = a[i]

        m = min(mx1, mx2, mx3)
        if a[i] > m:
            if m == mx1:
                mx1 = a[i]
            elif m == mx2:
                mx2 = a[i]
            else:
                mx3 = a[i]
    m1 = mn1 * mn2 * max(mx1, mx2, mx3)
    m2 = mx1 * mx2 * mx3
    return max(m1, m2)


for i in range(10000):
    a = random.sample(range(-10, 10), 5)
    if solution3(a) != solution2(a):
        print a, solution3(a), solution2(a)
