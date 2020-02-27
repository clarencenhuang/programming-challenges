"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

def reorder_list(head):
    arr = []
    cur = head
    while cur:
        arr.append(cur)
        cur = cur.next
    i, j = 0, len(arr) - 1
    prev = None
    while i <= j:
        if i < j:
            arr[i].next = arr[j]
        if prev:
            prev.next = arr[i]
        prev = arr[j]
        i += 1
        j -= 1
    if prev:
        prev.next = None
    return head


