""" Given a string s, return the longest substring p such that p > s lexicograhically"""


def compare(s, sub, l):
    for i in range(l):
        if s[i] == sub[i]:
            continue
        elif s[i] < sub[i]:
            return True
        else:
            return False
    return False


def longest_substring(s):
    for i in range(1, len(s)):
        if s[i] >= s[0] and compare(s, s[i:], len(s) - i):
            return s[i:]



print longest_substring('caddkfdsa')
print longest_substring('sst')
print longest_substring('ssat')
print longest_substring('dcbdcbx')
print longest_substring('dcbdcbax')
print longest_substring('google')
