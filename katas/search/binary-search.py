import random


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def binary_search_first_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    idx = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            idx = mid
            high = mid - 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return idx


def binary_search_last_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    idx = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            idx = mid
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return idx


def test_binary_search():
    a = random.sample(range(100), k=24)
    x = random.choice(a)
    a.sort()
    try:
        idx = a.index(x)
    except ValueError:
        idx = -1

    print(a, idx, x)
    assert idx == binary_search(a, x)


def test_binary_search_first_occurrence():
    a = [
        3,
        6,
        14,
        18,
        27,
        43,
        45,
        46,
        46,
        54,
        56,
        56,
        59,
        61,
        69,
        72,
        72,
        73,
        73,
        73,
        78,
        78,
        83,
        88,
    ]
    x = 56
    a.sort()
    assert 10 == binary_search_first_occurrence(a, x)


def test_binary_search_last_occurrence():
    a = [
        3,
        6,
        14,
        18,
        27,
        43,
        45,
        46,
        46,
        54,
        56,
        56,
        59,
        61,
        69,
        72,
        72,
        73,
        73,
        73,
        78,
        78,
        83,
        88,
    ]
    x = 56
    a.sort()
    assert 11 == binary_search_last_occurrence(a, x)
