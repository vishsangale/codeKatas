""" Implementation of merge sort
    Time complexity O(n*log(n))
    Space complexity O(n) """


def merge(l, r):
    nl = len(l)
    nr = len(r)
    out = [0] * (nl + nr)
    i = j = k = 0
    while i < nl and j < nr:
        if l[i] < r[j]:
            out[k] = l[i]
            i += 1
        else:
            out[k] = r[j]
            j += 1
        k += 1
    while i < nl:
        out[k] = l[i]
        i += 1
        k += 1

    while j < nr:
        out[k] = r[j]
        j += 1
        k += 1
    return out


def merge_sort(array):
    n = len(array)
    if n < 2:
        return array
    mid = n / 2
    l = merge_sort(array[:mid])
    r = merge_sort(array[mid:])
    return merge(l, r)


print merge_sort([5, 4, 3, 2, 1])
