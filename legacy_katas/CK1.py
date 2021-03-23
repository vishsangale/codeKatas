# ans = []


def answer(inp):
    ans = []
    for e in inp:
        if isinstance(e, list):
            ans += answer(e)
        else:
            ans.append(e)
    return ans


print answer([[1, 2, [3]], 4, [5, [6], [7, 8]]])
