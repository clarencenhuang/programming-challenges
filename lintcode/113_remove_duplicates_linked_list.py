from lintcode.datastructure_util import ListNode


def remove_dup(n):
    head, ptr = None, None
    cur = n
    while cur:
        nex = cur.next
        if nex and nex.val == cur.val:
            while nex and nex.val == cur.val:
                nex = nex.next
        else:
            if head is None:
                head, ptr = cur, cur
            else:
                ptr.next, ptr = cur, cur
        cur = nex
    if ptr:
        ptr.next = None
    return head


if __name__ == '__main__':
    ls = ListNode.create_from_string('1->1->1->1->null')
    print(remove_dup(ls))



