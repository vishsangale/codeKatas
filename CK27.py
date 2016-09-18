""" Given a string, please get the length of the longest substring which does not have duplicated characters. Supposing
    all characters in the string are in the range from a to z."""
from collections import Counter


def solution(a):
    last_str = ''
    m = 0
    for char in a:
        if last_str == '':
            last_str += char
        elif char not in last_str:
            last_str += char
        else:
            i = last_str.index(char)
            m = max(m, len(last_str))
            last_str += char
            last_str = last_str[i + 1:]
    return max(m, len(last_str))


def solution1(a):
    last_str = {}
    current = 0
    m = 0
    for i in range(len(a)):
        if a[i] not in last_str or i - last_str[a[i]] > current:
            current += 1
        else:
            m = max(m, current)
            current = i - last_str[a[i]]
        last_str[a[i]] = i
    return m


print solution('abxyabcxyzypqr'), solution1('abxyabcxyzypqr')
