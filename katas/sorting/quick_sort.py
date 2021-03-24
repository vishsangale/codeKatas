def partition(in_list, low, high):
    pivot = in_list[high]
    p_idx = low
    for i in range(low, high):
        if in_list[i] < pivot:
            in_list[i], in_list[p_idx] = in_list[p_idx], in_list[i]
            p_idx += 1

    in_list[p_idx], in_list[high] = in_list[high], in_list[p_idx]
    return p_idx


def _quick_sort(in_list, low, high):

    if low < high:
        pidx = partition(in_list, low, high)

        _quick_sort(in_list, low, pidx - 1)
        _quick_sort(in_list, pidx + 1, high)


def quick_sort(in_list):
    if not in_list:
        return in_list

    _quick_sort(in_list, 0, len(in_list) - 1)
