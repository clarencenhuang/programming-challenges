from typing import List
from heapq import heappush, heappop
from functools import reduce


def makelist(ls):
    return reduce(lambda a, x: ListNode(x, a), reversed(ls), None)


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __repr__(self):
        q = []
        cur = self
        while cur:
            q.append(str(cur.val))
            cur = cur.next
        return repr(','.join(q))


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for i, head in enumerate(lists):
            if head:
                heappush(heap, (head.val, i, head))
                lists[i] = lists[i].next

        head = None
        tail = None
        while heap:
            _, idx, node = heappop(heap)
            if head is None:
                head = tail = node
            else:
                tail.next = node
                tail = node
                node.next = None
            if lists[idx]:
                heappush(heap, (lists[idx].val, idx, lists[idx]))
                lists[idx] = lists[idx].next

        return head


if __name__ == '__main__':
    lsofls = [
        [1, 4, 5],
        [1, 3, 4],
        [2, 6]
    ]
    lists = [makelist(ls) for ls in lsofls]
    s = Solution()
    b = s.mergeKLists(lists)
    print(b)