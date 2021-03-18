

class Node:
    def __init__(self, _val, _next=None):
        self.val = _val
        self.next = _next


def find_merge_point(list1, list2):
    cur1 = list1
    len1 = 0
    while cur1:
        len1 += 1
        cur1 = cur1.next

    cur2 = list2
    len2 = 0
    while cur2:
        len2 += 1
        cur2 = cur2.next

    bigger_list = list1 
    if len1 > len2:
        bigger_list = list1
        smaller_list = list2
    else:
        bigger_list = list2
        smaller_list = list1

    diff = abs(len1 - len2)

    while diff > 0:
        bigger_list = bigger_list.next
        diff -= 1


    while bigger_list:
        if bigger_list.val == smaller_list.val:
            return bigger_list.val
        bigger_list = bigger_list.next
        smaller_list = smaller_list.next

    return None






