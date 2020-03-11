from lintcode.datastructure_util import RandomListNode


def copy_list(ln: RandomListNode):
    cur = ln
    while cur:
        cur_next = cur.next
        node = RandomListNode(cur.label)
        cur.next = node
        node.next = cur_next
        cur = cur_next

    cur = ln
    while cur:
        clone = cur.next
        if cur.random:
            clone.random = cur.random.next
        cur_next = clone.next
        cur = cur_next

    head = ln.next
    cur = head
    while cur and cur.next:
        next_cur = cur.next.next
        cur.next = next_cur
        cur = next_cur
    return head