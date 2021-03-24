
def merge(in_list, low, mid, high):

    idx = mid

    lowidx = low
    highidx = high

    while lowidx <  mid and highidx > mid:
        if in_list[lowidx] > in_list[highidx]:
            in_list[lowidx], in_list[highidx] = in_list[highidx] > in_list[lowidx]
        lowidx += 1
        highidx -= 1

def _merge_sort(in_list, low, high):

    m = low + (high - 1) // 2

    if high > 1:
        _merge_sort(in_list, low, mid)
        _merge_sort(in_list, mid + 1, high)

        merge(in_list, low, m, right)

def merge_sort(in_list):
    if not in_list:
        return in_list

    _merge_sort(in_list, 0, len(in_list) - 1)
