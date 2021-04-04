def jumpingOnClouds(c):
    jumps = 0
    idx = 0
    while idx < len(c) - 1:
        if idx + 2 < len(c) and not c[idx + 2]:
            idx += 2
        elif idx + 1 < len(c) and not c[idx + 1]:
            idx += 1
        jumps += 1
    return jumps


def test_jumping():
    assert 4 == jumpingOnClouds([0, 0, 1, 0, 0, 1, 0])
    assert 3 == jumpingOnClouds([0, 0, 0, 0, 1, 0])
