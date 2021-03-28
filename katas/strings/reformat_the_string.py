"""Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.

"""


def reformat(s: str) -> str:
    if not s:
        return s

    nums = []
    chars = []
    for char in s:
        if char.isdigit():
            nums.append(char)
        elif char.isalpha():
            chars.append(char)

    if abs(len(chars) - len(nums)) > 1:
        return ""
    ans = [""] * len(s)
    l_idx = 0
    s_idx = 0
    if len(chars) != len(nums):
        large_list = chars if len(chars) > len(nums) else nums
        small_list = chars if len(nums) > len(chars) else nums
    else:
        large_list = nums
        small_list = chars
    for i in range(len(s)):
        if i % 2 == 0:
            ans[i] = large_list[l_idx]
            l_idx += 1
        else:
            ans[i] = small_list[s_idx]
            s_idx += 1
    return "".join(ans)


def test_reformat():

    assert "0a1b2c" == reformat("a0b1c2")

    assert "" == reformat("elite")

    assert "" == reformat("elite012")

    assert "e0l1i2t3e" == reformat("elite0123")

    assert "c2o0v1i9d" == reformat("covid2019")
