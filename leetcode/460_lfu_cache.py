class Node:

    def __init__(self, key, val, freq=0, nex=None, pre=None):
        self.val = val
        self.key = key
        self.nex = nex
        self.pre = pre
        self.freq = freq

    def __repr__(self):
        rep = str(self.val)
        cur = self.nex
        while cur:
            rep += f",{cur.val}"
            cur = cur.nex
        return repr(rep)


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.num = 0
        self.head = None
        self.tail = None

    def _incre_freq(self, n):
        n.freq += 1
        while n.pre and n.freq >= n.pre.freq:
            # swap n and n prev
            n_nex = n.nex
            n_pre = n.pre
            n_pre_pre = n_pre.pre

            # hookup self with prev
            n.nex = n_pre
            n_pre.pre = n

            # hookup prev to next
            n_pre.nex = n_nex
            if n_nex:
                n_nex.pre = n_pre
            # update tail
            if self.tail == n:
                self.tail = n_pre
            # hookup self with prev prev
            n.pre = None
            if n_pre_pre:
                n.pre = n_pre_pre
                n_pre_pre.nex = n
        if n.pre is None:
            self.head = n

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        n = self.cache[key]
        self._incre_freq(n)
        return n.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.cache:
            n = self.cache[key]
            n.val = value
            self._incre_freq(n)
        else:
            if self.num >= self.capacity:
                tail_pre = self.tail.pre
                del self.cache[self.tail.key]
                self.tail = tail_pre
                if tail_pre:
                    tail_pre.nex = None
                else:
                    self.head = None
                self.num -= 1
            n = Node(key, value)
            self.cache[key] = n
            if self.head is None:
                self.head = self.tail = n
            else:
                cur = self.tail
                while cur and cur.val <= n.val:
                    cur = cur.pre
                if cur:
                    cur_nex = cur.nex
                    n.nex = cur_nex
                    if cur_nex:
                        cur_nex.pre = n
                    else:
                        self.tail = n
                    cur.nex = n
                    n.pre = cur
                else:
                    n.nex = self.head.nex
                    n.pre = None
                    self.head = n
            self.num += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    #["LFUCache", "put", "put", "put", "put", "get", "get", "get", "get", "put", "get", "get", "get", "get", "get"]
    cmds = [[1, 1], [2, 2], [3, 3], [4, 4], [4], [3], [2], [1], [5, 5], [1], [2], [3], [4], [5]]
    #cmds = [[2,2],[1,1],[2],[1],[2],[3,3],[4,4],[3],[2],[1],[4]]
    s = LFUCache(3)
    for cmd in cmds:
        if len(cmd) == 2:
            s.put(cmd[0], cmd[1])
        else:
            print(s.get(cmd[0]))

