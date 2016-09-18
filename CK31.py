""" Write a function that takes as input an array of integers A, and two integers low and high.
    Your function has to output pairs {(x,y), ...}
    Where each pair of denotes that the sub-array of A[i...j] has a sum in the range low <= sum <= high. """


def solution(arr, low, high):
    out = []
    n = len(arr)
    for i in range(n):
        current_sum = arr[i]
        if low <= current_sum <= high:
            out.append([arr[i]])
        for j in range(i + 1, n):
            if current_sum + arr[j] <= high:
                current_sum += arr[j]
            elif current_sum + arr[j] > high:
                break
            if low <= current_sum <= high:
                out.append(arr[i:j + 1])
    return out


print solution([3, 2, 0, -1, 4, 5], 2, 8)


