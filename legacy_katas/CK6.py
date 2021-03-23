""" Replace all spaces with given characters
    Time complexity O(n)
    Space Complexity O(n)
    """


def answer(string, chars):
    out_string = []
    for s in string:
        if s == " ":
            out_string.append(chars)
        else:
            out_string.append(s)
    return "".join(out_string)


print answer("ad bh sfj ds haf", "%20")
