"""Given two strings, a string swap of any two indices, could make the strings equal. Indices can be same"""


def test_strings_equal():

    assert True == one_swap_away_strings("hello", "hello")
    assert False == one_swap_away_strings("", "hello")
    assert False == one_swap_away_strings("hello", "")
    assert False == one_swap_away_strings("hell", "hello")

    assert True == one_swap_away_strings("hello", "oellh")


def one_swap_away_strings(s1: str, s2: str) -> bool:

    if not s1 or not s2:
        return False

    if len(s1) != len(s2):
        return False

    if s1 == s2:
        return True
    diff = []
    for i, (s1_char, s2_char) in enumerate(zip(s1, s2)):
        if s1_char != s2_char:
            diff.append(i)

    if len(diff) != 2:
        return False
    else:
        s2_new = list(s2)
        s2_new[diff[0]], s2_new[diff[1]] = s2_new[diff[1]], s2_new[diff[0]]
        s2_new = "".join(s2_new)
        if s1 == s2_new:
            return True
    """
    # Brute force approach
    s2 = list(s2)
    for i in range(len(s2)):
        for j in range(len(s2)):
            new_s2 = list(s2)
            new_s2[i], new_s2[j] = new_s2[j], new_s2[i]
            if s1 == "".join(new_s2):
                return True
    """
    return False
