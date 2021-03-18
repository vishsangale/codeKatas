""" Insertion Sort
    Time Complexity O(n^2)
    Space Complexity O(1) """


def insertion_sort(inp):
    n = len(inp)
    for i in range(n):
        current = inp[i]
        pivot = i
        while pivot > 0 and inp[pivot - 1] > current:
            inp[pivot] = inp[pivot - 1]
            pivot -= 1
        inp[pivot] = current
    return inp


print insertion_sort([2, 45, 13, 43, 32, 3443, 43])
