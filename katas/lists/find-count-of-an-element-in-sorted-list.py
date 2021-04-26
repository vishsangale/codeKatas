def find_count(arr, target):
    count = 0
    if not arr:
        return count

    low = 0
    high = len(arr) - 1
    idx = 0
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            count += 1
            idx = mid
            break
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    low_idx = idx - 1
    while low_idx and arr[low_idx] == target:
        count += 1
        low_idx -= 1
    high_idx = idx + 1
    while high_idx < len(arr) and arr[high_idx] == target:
        count += 1
        high_idx += 1

    return count


def test():
    a = [
        1,
        1,
        3,
        4,
        4,
        6,
        9,
        11,
        13,
        13,
        14,
        14,
        15,
        16,
        18,
        19,
        20,
        21,
        21,
        22,
        22,
        24,
        26,
        27,
        28,
        30,
        32,
        33,
        34,
        37,
        38,
        41,
        41,
        42,
        43,
        47,
    ]
    x = 21
    assert 2 == find_count(a, x)

    a = [1, 1, 3, 4, 4, 6, 6, 6, 6, 6, 6]
    x = 21
    assert 0 == find_count(a, x)

    a = [1, 1, 3, 4, 4, 6, 6, 6, 6, 6, 6]
    x = 6
    assert 6 == find_count(a, x)
