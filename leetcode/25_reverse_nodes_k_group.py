from functools import reduce
from collections import deque


class ListNode:

    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __repr__(self):
        q = []
        cur = self
        seen = set()
        while cur and cur not in seen:
            seen.add(cur)
            q.append(str(cur.val))
            cur = cur.next

        return repr(','.join(q))


def makelist(ls):
    return reduce(lambda a, x: ListNode(x, a), reversed(ls), None)


def reverse_k(head, k):
    q = deque()
    first_head = None
    last_head = None
    cur = head
    while cur:
        cur_nex = cur.next
        q.append(cur)
        if len(q) == k:
            while q:
                n = q.pop()
                if first_head is None:
                    first_head = n
                if last_head:
                    last_head.next = n
                last_head = n
            last_head.next = None
        cur = cur_nex
    while q:
        n = q.popleft()
        if first_head is None:
            first_head = n
        if last_head:
            last_head.next = n
        last_head = n
    last_head.next = None
    return first_head


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        return reverse_k(head, k)

if __name__ == '__main__':
    s = Solution()
    ls = makelist([1,2,3,4,5])
    res = s.reverseKGroup(ls, 2)
    print(res)