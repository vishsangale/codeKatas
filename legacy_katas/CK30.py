""" https://www.interviewcake.com/question/python/matching-parens
    I like parentheticals (a lot). "Sometimes (when I nest them (my parentheticals) too much (like this (and this)))
    they get confusing."
    Write a function that, given a sentence like the one above, along with the position of an opening parenthesis,
    finds the corresponding closing parenthesis.
    Example: if the example string above is input with the number 10 (position of the first parenthesis),
    the output should be 79 (position of the last parenthesis).
"""


def solution(s, inp):
    if not s:
        return -1
    if 0 >= inp > len(s):
        return -1
    braces = []
    for i in range(len(s)):
        if s[i] == "(":
            braces.append(i)
        elif s[i] == ")":
            item = braces.pop()
            if item == inp:
                return i
    return -1


s = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
# s = ''
print solution(s, 10)
