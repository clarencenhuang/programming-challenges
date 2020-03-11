from lintcode.datastructure_util import ListNode

def merge2(a1: ListNode, a2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    cur = dummy
    while a1 or a2:
        if not a2 or (a1 and a1.val <= a2.val):
            cur.next, cur, a1 = a1, a1, a1.next
        elif not a1 or (a2 and a2.val <= a1.val):
            cur.next, cur, a2 = a2, a2, a2.next

    return dummy.next

