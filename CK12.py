import random


def find_profit(a):
    n = len(a)
    max_profit = a[1] - a[0]
    for i in range(n):
        for j in range(i + 1, n):
            # if a[i] < a[j]:
            max_profit = max(max_profit, a[j] - a[i])
    return max_profit


def find_profit_1(a):
    min_val = a[0]
    max_profit = a[1] - a[0]
    for i in range(1, len(a)):
        current_profit = a[i] - min_val
        max_profit = max(max_profit, current_profit)
        min_val = min(min_val, a[i])
    return max_profit


""" This implementation does not work if array is arranged in decreasing order."""


def find_profit_2(a):
    min_index = a.index(min(a))
    max_index = a.index(max(a))
    if min_index < max_index:
        return max(a) - min(a)
    elif min_index == max_index:
        return 0
    elif max_index < min_index:
        if a[:max_index] and a[min_index:]:
            new_min = min(a[:max_index])
            new_max = max(a[min_index:])
            max_bet = find_profit_2(a[max_index:min_index])
            return max(a[max_index] - new_min, new_max - a[min_index], max_bet)
        elif len(a[:max_index]) > 1:
            new_min = min(a[:max_index])
            max_bet = find_profit_2(a[max_index:min_index])
            return max(a[max_index] - new_min, max_bet)
        elif len(a[min_index:]) > 1:
            new_max = max(a[min_index:])
            max_bet = find_profit_2(a[max_index:min_index])
            return max(new_max - a[min_index], max_bet)
        else:
            return find_profit_2(a[max_index:min_index])


# A = [10, 7, 5, 8, 11, 9]

B = [9, 7, 5, 4, 3]
C = [6, 5, 4, 3, 2, 1]
# print find_profit_2(B)
for i in range(1000):
    A = random.sample(range(2, 10), 5)
    if find_profit_1(A) != find_profit_2(A):
        print A, find_profit_1(A), find_profit_2(A)
# print find_profit(B), find_profit_1(B), find_profit_2(B)
# print find_profit(C), find_profit_1(C), find_profit_2(C)
