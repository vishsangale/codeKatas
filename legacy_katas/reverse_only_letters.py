def reverseOnlyLetters(s):

    start = 0
    end = len(s) - 1
    reversed_string = []
    for i in range(end, -1, -1):
        if s[i].isAlpha():
            reversed_string.append(s[i])


def spiral_order(matrix):
    out = []
    if not matrix:
        return out

    row_begin = 0
    row_end = len(matrix)
    col_begin = 0
    col_end = len(matrix)

    while row_begin < row_end and col_begin < col_end:

        for i in range(col_begin, col_end):
            out.append(matrix[row_begin][i])

        row_begin += 1

        for j in range(row_begin, row_end):
            out.append(matrix[j][col_end - 1])

        col_end -= 1
    return out


print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
