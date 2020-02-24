
class Node:


    def __init__(self, lo, hi, val = 0):
        self.hi = hi
        self.lo = lo
        self.mid = (lo + hi) // 2
        self.left = self.right = None
        self.val = val

    @property
    def is_leaf(self):
        return self.left is None and self.right is None

    def update(self, lo, hi, val):
        if hi <= self.lo or lo >= self.hi:
            return

        if lo <= self.lo and hi >= self.hi:
            self.val = val
            self.left = None
            self.right = None
        else:
            if not self.left:
                self.left = Node(self.lo, self.mid, self.val)
            if not self.right:
                self.right = Node(self.mid, self.hi, self.val)
            self.left.update(lo, hi, val)
            self.right.update(lo, hi, val)
            self.val = max(self.left.val, self.right.val)

    def query(self, lo, hi):
        if hi <= self.lo or lo >= self.hi:
            return 0

        # if there is some overlap and i'm the only node covering this range
        if self.is_leaf:
            return self.val
        else:
            # else do more fine grained queries
            return max(self.left.query(lo, hi), self.right.query(lo, hi))