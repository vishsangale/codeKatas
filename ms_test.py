import collections


def concat(arr):
    m = collections.defaultdict(list)
    for i, st in enumerate(arr):
        if len(set(st)) != len(st):
            continue
        m[len(st)].append(i)
    lst = []
    for size in sorted(m, reverse=True):
        lst += m[size]
    res = 0
    print(m)
    print(lst)
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            idx1, idx2 = lst[i], lst[j]
            if not (set(arr[idx1]) & set(arr[idx2])):
                return len(arr[idx1]) + len(arr[idx2])
    return 0


def maxLength(arr) -> int:
    comb = [set(word) for word in arr if len(set(word)) == len(word)]
    ret = [set()]
    for charSet in comb:
        for wordSet in comb:
            if not (charSet & wordSet):
                ret.append(charSet | wordSet)
    if len(ret) == 1:
        return 0
    for charSet in comb:
        for wordSet in ret:
            if not (charSet & wordSet):
                ret.append(charSet | wordSet)

    return max(len(charSet) for charSet in ret)


a = [1, 2, 3, 4]
print(a[:2], a[2:])
