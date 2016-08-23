ans = []

def answer(inp):
    for e in inp:
        if isinstance(e, list):
            answer(e)
        else:
            ans.append(e)
    return ans


print answer([[1,2,[3]],4,[5, [6], [7, 8]]])