# import random
#
#
# def selection_sort(A):
#     l = len(A)
#
#     for i in range(l):
#         i_min = i
#         for j in range(i + 1, l):
#             if A[i] > A[j]:
#                 i_min = j
#
#         A[i_min], A[i] = A[i], A[i_min]
#
#
# def bubble_sort(A):
#     l = len(A)
#     for i in range(l):
#         for j in range(0, l - 1):
#             if A[j] > A[j + 1]:
#                 A[j], A[j + 1] = A[j + 1], A[j]
#
#
# def insertion_sort(A):
#     for i in range(1, len(A)):
#         val = A[i]
#         hole = i
#         while hole > 0 and A[hole - 1] > val:
#             A[hole] = A[hole - 1]
#             hole = hole - 1
#
#         A[hole] = val
#
#
# A = random.sample(range(10, 30), 10)
#
# print(A)
# insertion_sort(A)
# print(A)


def sumsDivisibleByK(a, k):
    count = 0
    a = sorted(a)

    divisors = [0] * k
    for item in a:
        divisors[item % k] += 1
    count = divisors[0] * (divisors[0] - 1) / 2

    if k // 2 == 1:
        count += divisors[k // 2] * divisors[k - k // 2 - 1]

    for i in range(1, k // 2):
        print(i)
        print(i, divisors[i] * divisors[k - i - 1])
        count += divisors[i] * divisors[k - i - 1]

    i = 1
    # while (i <= k//2) and i != (k -i):
    #     print(i)
    #     count += divisors[i] * divisors[k-i]
    #     i += 1

    if k % 2 == 0:
        count += divisors[k // 2] * (divisors[k // 2] - 1) / 2

    # for i in range(len(a)):
    #     for j in range(i + 1, len(a)):
    #         print(a[i] + a[j], (a[i] + a[j]) % k)
    #         if a[i] + a[j] % k == 0:
    #             count += 1

    return count


# print(sumsDivisibleByK([51, 24, 44, 87, 64, 84, 76, 47, 31, 21, 34, 49, 30, 70, 83, 3, 38, 6, 99, 7, 92, 59, 57, 50, 73, 79, 93, 19, 68, 72, 23, 90, 71, 35, 77, 28, 36, 45, 94, 29, 39, 98, 48, 9, 60, 20, 62, 100, 1, 97, 16, 66, 56, 54, 80, 15, 46, 18, 2, 88, 8, 65, 69, 78, 40, 37, 33, 25, 89, 13, 85, 5, 32, 86, 11, 52, 63, 67, 12, 55, 82, 43, 81, 91, 26, 27, 95, 58, 75, 61, 41, 17, 14, 10, 96, 53, 4, 22, 74, 42], 10))

print(sumsDivisibleByK([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
