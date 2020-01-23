"""Numbers With Equal Digit Sum

    Given an array consisting of N integers, return the maximum sum of two
    numbers whose digits add up to an equal sum. If there are no two numbers 
    whose digits have an equal sum , then return -1.
"""

import unittest


def get_digits_sum(num):
    num = abs(num)
    digits_sum = 0
    while num:
        digits_sum += num % 10
        num = num // 10
    return digits_sum


def find_solution(in_array):
    max_sum = -1
    max_sum_dict = dict()

    for num in in_array:
        digits_sum = get_digits_sum(num)

        if digits_sum in max_sum_dict:
            other_num = max_sum_dict[digits_sum]
            max_sum = max(max_sum, num + other_num)
            max_sum_dict[digits_sum] = max(num, other_num)
        else:
            max_sum_dict[digits_sum] = num 

    return max_sum

class TestMethods(unittest.TestCase):
    def test_get_digits_sum(self):
        self.assertEqual(18, get_digits_sum(4653))

        self.assertEqual(18, get_digits_sum(-4653))

        self.assertEqual(13, get_digits_sum(463))

        self.assertEqual(3, get_digits_sum(3))


    def test_find_solution(self):

        self.assertEqual(93, find_solution([51, 71, 17, 42]))

        self.assertEqual(102, find_solution([42, 33, 60]))

        self.assertEqual(-1, find_solution([51, 32, 43]))


if __name__ == '__main__':
    unittest.main()

