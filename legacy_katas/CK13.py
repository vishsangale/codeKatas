import random


def binary_search(a, x):
    n = len(a) / 2
    if x == a[n]:
        return True
    if x > a[n]:
        return binary_search(a[n:], x)
    elif x < a[n]:
        return binary_search(a[:n], x)
    else:
        return False


# binary_search([3, 4, 5, 7, 9], 3)
for i in range(10000000):
    A = random.sample(range(2, 10), 5)
    A.sort()
    x = random.randint(2, 10)

    if x in A and not binary_search(A, x):
        print A, x, binary_search(A, x)
