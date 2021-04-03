"""
Given an numbersay of integers numbers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer numbersay answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

You may assume that each input would have exactly one solution and you may not use the same element twice.
"""


def two_sum(numbers, target):

    # for i in range(len(numbers)):
    #     for j in range(i + 1, len(numbers)):
    #         if numbers[i] + numbers[j] == target:
    #             return [i + 1, j + 1]

    numbers_d = {key: val for val, key in enumerate(numbers)}
    for num in numbers_d:
        if target - num in numbers_d:
            if num == target - num:
                idx = numbers.index(num) + 1
                return [idx, idx + 1]
            return [numbers_d[num] + 1, numbers_d[target - num] + 1]


def test_two_sum():
    assert [1, 2] == two_sum([2, 7, 11, 15], 9)
    assert [1, 3] == two_sum([2, 3, 4], 6)
    assert [1, 2] == two_sum([-1, 0], -1)
