from functools import reduce


class RandomListNode:

    def __init__(self, x, next=None, random=None):
        self.label = x
        self.next = next
        self.random = random


class ListNode:

    def __init__(self, x, nex:'ListNode'=None):
        self.val = x
        self.next = nex

    def __repr__(self):
        q = []
        cur = self
        seen = set()
        while cur:
            if cur in seen:
                q.append(f'LOOP({cur.val})')
                break
            seen.add(cur)
            q.append(str(cur.val))
            cur = cur.next
        return repr(','.join(q))

    @staticmethod
    def create_from_array(ls):
        return reduce(lambda a, x: ListNode(x, a), reversed(ls), None)

    @staticmethod
    def create_from_string(s):
        parts = s.split('->')
        if parts[-1] == 'null':
            parts = parts[:-1]
        ls = list(map(int, parts))
        return ListNode.create_from_array(ls)


class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

