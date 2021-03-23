def solution(a):
    m = 0
    current = a[0]
    count = 0
    for i in range(1, len(a)):
        if a[i] < current:
            current = a[i]
            count = 0
        else:
            count += 1
            m = max(count, m)
    return m


print solution([10, 4, 6, 2, 8, 9, 4])
print solution([10, 9, 8, 7, 6, 5, 4])
