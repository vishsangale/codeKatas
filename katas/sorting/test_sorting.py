import random
import pytest

from katas.sorting.quick_sort import quick_sort
from katas.sorting.merge_sort import merge_sort


@pytest.mark.parametrize("fn", [quick_sort, merge_sort])
def test_quick_sorting(fn):
    l = []

    quick_sort(l)

    assert [] == l
    k = 20
    l = random.sample(range(1, 100), k)
    assert k == len(l)

    fn(l)

    assert l == sorted(l)

    # pass sorted list
    l.sort()
    fn(l)
    assert l == sorted(l)
