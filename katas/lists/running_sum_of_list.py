"""Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i])."""


def test_running_sum():

    assert [] == running_sum([])

    assert [-1] == running_sum([-1])

    assert [1, 3, 6, 10] == running_sum([1, 2, 3, 4])


def running_sum(l):
    if not l:
        return l
    current_sum = 0
    for i, val in enumerate(l):
        current_sum += val
        l[i] = current_sum

    return l
