""" Encoder to compress string whenever possible.
    p14akkkkkkkkpq -> p14a8xkpq
    the only requirement is encodings should be unambiguous"""


def solution(a):
    out = ""
    last_char = ""
    current_char = ""
    count = 0
    for char in a:
        if current_char == char:
            if last_char.isdigit():
                last_char = current_char
                current_char = char
                out += current_char
                count = 1
                continue
            count += 1
            if count == 9:
                out += "9x" + current_char
                count = 0
        elif current_char == "":
            current_char = char
            last_char = char
            count += 1
        elif count > 3:
            out += str(count) + "x" + current_char
            current_char = ""
            count = 0
        else:
            out += current_char * count
            last_char = current_char
            current_char = char
            count = 1
    if count > 3:
        out += str(count) + "x" + current_char
    else:
        out += current_char * count
    return out


print solution("1aaaaa")
