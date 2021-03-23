""" There are n houses built in a line, each of which contains some value in it. A thief is going to steal the maximal
    value in these houses, but he cannot steal in two adjacent houses because the owner of a stolen house will tell his
    two neighbors on the left and right side. What is the maximal stolen value?"""


def solution(a):
    n = len(a)
    if n <= 0:
        return 0
    prev = a[0]
    if n == 1:
        return prev
    current_max = max(a[0], a[1])
    if n == 2:
        return current_max
    total = 0
    for i in range(2, n):
        total = max(current_max, prev + a[i])
        prev, current_max = current_max, total
    return total


print solution([6, 7, 2, 7])
