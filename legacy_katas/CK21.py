import time


def max_multiple_length(l):
    max_len = float("-inf")
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if not overlap(l[i], l[j]):
                mult = len(l[i]) * len(l[j])
                max_len = max(mult, max_len)
    return max_len


def overlap(word1, word2):
    letter_set = set(word1)
    for c in word2:
        if c in letter_set:
            return True
    return False


def max_multiple_length1(l):
    max_len = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            mul = len(l[i]) * len(l[j])
            if mul > max_len and overlap1(l[i], l[j]):
                max_len = max(mul, max_len)
    return max_len


def overlap1(word1, word2):
    return set(word1).isdisjoint(set(word2))


if __name__ == "__main__":
    l = ["ABCW", "BAZ", "FOO", "BAR", "XTFN", "ABCDEF"] * 1000
    # t = time.time()
    # print max_multiple_length(l)
    # print time.time() - t
    t = time.time()
    print max_multiple_length1(l)
    print time.time() - t
