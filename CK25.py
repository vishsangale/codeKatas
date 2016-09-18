import sys


def get_min_change(coins, amount):
    counts = [None] * (amount + 1)
    counts[0] = 0
    for i in range(1, amount + 1):
        count = sys.maxint
        for coin in coins:
            if i - coin >= 0:
                count = min(count, counts[i - coin])
        counts[i] = count + 1
    return counts


""" This below function does not work!!!!"""


def get_min_change_rec(coins, amount):
    if amount == 1:
        return 1
    for coin in coins:
        return get_min_change_rec(coins, amount - coin) + 1


print get_min_change([1, 5, 10, 25], 99), get_min_change_rec([1, 5, 10, 25], 99)
