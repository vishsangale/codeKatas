#!/usr/bin/env python3

def pascal_triangle_rec(n, k, triangle):
    if k == 0 or k == n:
        return 1

    return pascal_triangle_rec(n - 1, k, triangle) + pascal_triangle_rec(n - 1, k - 1, triangle)


def pascal_triangle(n: int, k: int) -> int:
    triangle = []
    for row in range(n + 1):
        cur = []
        for col in range(row + 1):
            cur.append(pascal_triangle_rec(row, col, triangle))
        triangle.append(cur)
    # for tri in triangle:
    #     print(tri)
    return triangle[n][k]


def main():
    """
    1 - (0, 0)
    1 - (1, 0)  1 (1, 1)
    1 - (2, 0), 2 (2, 1) , 1(2, 2)
    """
    print(pascal_triangle(0, 0))
    print(pascal_triangle(2, 1))
    print(pascal_triangle(5, 2))
    print(pascal_triangle(6, 6))


main()