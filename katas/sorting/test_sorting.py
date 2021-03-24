import random

from katas.sorting.quick_sort import quick_sort


def test_quick_sorting():
    l = []

    quick_sort(l)

    assert [] == l
    k = 20
    l = random.sample(range(1, 100), k)
    assert k == len(l)

    quick_sort(l)

    assert l == sorted(l)

    # pass sorted list
    l.sort()
    quick_sort(l)
    assert l == sorted(l)
