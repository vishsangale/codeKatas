from collections import Counter


def check_insert_remove(str1, str2):
    if len(str1) > len(str2):
        large = Counter(str1)
        small = Counter(str2)
    else:
        large = Counter(str2)
        small = Counter(str1)

    found_diff = False

    for char in large:
        if large[char] != small[char]:
            if found_diff:
                return False
            found_diff = True

    return True


def check_replace(str1, str2):
    found_diff = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if found_diff:
                return True
            found_diff = True
    return True


def solve(str1, str2):
    if len(str1) != len(str2):
        return check_insert_remove(str1, str2)
    return check_replace(str1, str2)


def solve2(str1, str2):
    if len(str1) < len(str2):
        short = str1
        long = str2
    else:
        short = str2
        long = str1

    found_diff = False
    short_idx = 0
    long_idx = 0
    while short_idx < len(short) and long_idx < len(long):
        if short[short_idx] != long[long_idx]:
            if found_diff:
                return False
            found_diff = True
            if len(short) == len(long):
                short_idx += 1
        else:
            short_idx += 1
        long_idx += 1
    return True


print(solve2("pale", "ple"))
print(solve2("pale", "bale"))
print(solve2("pale", "bales"))
print(solve2("pale", "pales"))
