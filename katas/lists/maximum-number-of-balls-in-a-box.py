"""
You are working in a ball factory where you have n balls numbered from lowLimit up to highLimit inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes numbered from 1 to infinity.

Your job at this factory is to put each ball in the box with a number equal to the sum of digits of the ball's number. For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6 and the ball number 10 will be put in the box number 1 + 0 = 1.

Given two integers lowLimit and highLimit, return the number of balls in the box with the most balls.
"""
from collections import Counter


def get_box_num(i):
    box_num = 0
    while i:
        box_num += i % 10
        i = i // 10
    return box_num


def count_balls(lowLimit: int, highLimit: int) -> int:
    boxes = Counter()
    for i in range(lowLimit, highLimit + 1):
        boxes[get_box_num(i)] += 1
    return max(boxes.values())


def test_count_balls():

    assert 2 == count_balls(1, 10)

    assert 2 == count_balls(19, 28)

    assert 2 == count_balls(5, 15)

    assert 1 == count_balls(1, 4)
