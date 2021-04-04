def merge(left, right, out):
    out.clear()

    l_idx = 0
    r_idx = 0

    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] < right[r_idx]:
            out.append(left[l_idx])
            l_idx += 1
        else:
            out.append(right[r_idx])
            r_idx += 1

    while l_idx < len(left):
        out.append(left[l_idx])
        l_idx += 1

    while r_idx < len(right):
        out.append(right[r_idx])
        r_idx += 1


def merge_sort(in_list):
    if not in_list:
        return in_list

    if len(in_list) < 2:
        return in_list

    mid =  len(in_list) // 2
    left = in_list[:mid]
    right = in_list[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left, right, in_list)

