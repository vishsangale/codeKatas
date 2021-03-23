def replace_space(str_list, idx):
    for char in "02%":
        str_list[idx] = char
        idx -= 1


def solve(in_str):
    str_list = list(in_str)

    first_char_from_rev = len(str_list) - 1
    for i in range(len(str_list) - 1, -1, -1):
        if str_list[i] != " ":
            first_char_from_rev = i
            break
    cur_idx = len(str_list) - 1
    for i in range(first_char_from_rev, -1, -1):
        if str_list[i] != " ":
            str_list[cur_idx] = str_list[i]
            cur_idx -= 1
            # str_list[i] = " "
        else:
            replace_space(str_list, cur_idx)
            cur_idx -= 3

    return "".join(str_list)


inp = "Mr John S    "

print(solve(inp))
