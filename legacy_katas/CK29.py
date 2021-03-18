""" Given the list of IDs, which contains many duplicate integers and one unique integer, find the unique integer
"""
from collections import Counter

""" Time complexity O(n)
    Space complexity O(n)"""


def solution(ids):
    n = len(ids)
    if n <= 2:
        return -1
    hash_ids = Counter()

    for id in ids:
        hash_ids[id] += 1

    for key in hash_ids.keys():
        if hash_ids[key] == 1:
            return key
    return -1


""" Time complexity O(n*lg(n))
    Space complexity O(1) -  if we used in-place algorithms like quick-sort"""


def solution1(ids):
    ids.sort()
    n = len(ids)
    if n <= 2:
        return -1
    if ids[0] != ids[1]:
        return ids[0]
    if ids[n - 1] != ids[n - 2]:
        return ids[n - 1]
    for i in range(1, n - 1):
        if ids[i - 1] != ids[i] and ids[i] != ids[i + 1]:
            return ids[i]
    return -1


a = [3, 1, 2, 3, 4, 3, 2, 1]
print solution(a), solution1(a)
