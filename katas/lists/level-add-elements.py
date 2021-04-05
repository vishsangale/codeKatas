

def update_past(data, n, current_idx , diff):
    if diff <= 0:
        return n

    eq = diff // (current_idx + 1)
    rem = diff % (current_idx + 1)
    if eq == 0:
        return update_past(data, n, current_idx - 1, rem)
    for i in range(current_idx + 1):
        if n > 0:
            data[i] += eq
            n -= eq
        else:
            break
    return update_past(data, n, current_idx, rem)


def add_elements(data, n):

    if n <= 0:
        return data

    data.sort()

    while n > 0:
        for i in range(len(data) - 1):
            diff = data[i + 1] - data[i]
            n = update_past(data, n, i, diff)
            print(data)
            if n == 0:
                break
    return data

def test_add_elements():
    assert [5, 5, 5, 9] == add_elements([2, 4, 1, 9], 8)
    assert [6, 5, 5, 9] == add_elements([2, 4, 1, 9], 9)
