# ls = [(65, 100), (70, 150), (100, 90), (75, 190), (60, 95), (68, 110)]

ls = [(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)]


def find_max_seq_l(ls, unfit):
    n = len(ls)
    seq = 0
    pht = 0
    pwt = 0
    new_unfit = 0
    if unfit >= n:
        return 0
    for i in range(unfit, n):
        if ls[i][0] > pht and ls[i][1] > pwt:
            seq += 1
            pht = ls[i][0]
            pwt = ls[i][1]
        elif unfit == 0:
            new_unfit = i
    if new_unfit == 0:
        return seq
    return max(seq, find_max_seq_l(ls, new_unfit))


def find_max_seq(ls):
    ls.sort(key=lambda x:(x[0], x[1]))
    print ls
    return find_max_seq_l(ls, 0)

print find_max_seq(ls)
