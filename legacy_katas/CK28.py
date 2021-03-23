""" https://www.interviewcake.com/question/python/inflight-entertainment
    You've built an in-flight entertainment system with on-demand movie streaming.
    Users on longer flights like to start a second movie right when their first one ends, but they complain that the
    plane usually lands before they can see the ending. So you're building a feature for choosing two movies whose total
    runtimes will equal the exact flight length.
    Write a function that takes an integer flight_length (in minutes) and a list of integers movie_lengths (in minutes)
    and returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.
"""
import random

""" Time complexity O(n^2)
    Space complexity O(1)
    """


def solution(flight_length, movie_lengths):
    n = len(movie_lengths)
    if n < 2:
        return False
    for i in range(n):
        for j in range(i + 1, n):
            if movie_lengths[i] + movie_lengths[j] == flight_length:
                return True

    return False


""" Time complexity O(n*lg(n))
    Space complexity O(1) if used in-place sorting algorithm like quick-sort
    """


def solution1(flight_length, movie_lengths):
    movie_lengths.sort()
    left = 0
    right = len(movie_lengths) - 1
    while left < right:
        if movie_lengths[left] + movie_lengths[right] == flight_length:
            return True
        elif movie_lengths[left] + movie_lengths[right] < flight_length:
            left += 1
        else:
            right -= 1

    return False


for i in range(100000):
    fl = random.randint(30, 200)
    ml = random.sample(range(30, 180), 100)
    if solution(fl, ml) != solution1(fl, ml):
        print fl, ml
