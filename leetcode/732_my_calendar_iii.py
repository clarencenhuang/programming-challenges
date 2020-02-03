from bisect import bisect
import math

class MyCalendarThree:

    def __init__(self):
        self.nodes = []
        self.nid = 0
        self.node_info = {}
        self.val2node = {}

    def _get_node(self, val):
        if val in self.val2node:
            return self.val2node[val]
        node = (val, set(), set())
        self.val2node[val] = node
        idx = bisect(self.nodes, node)
        self.nodes.insert(idx, node)
        return node

    def book(self, start: int, end: int) -> int:
        # insert start end into sorted
        self.nid += 1
        start_node = self._get_node(start)
        end_node = self._get_node(end)
        start_node[1].add(self.nid)
        end_node[2].add(self.nid)
        self.node_info[self.nid] = (start, end)
        idx_start, idx_end = bisect(self.nodes, start_node) - 1, bisect(self.nodes, end_node) - 1
        # look at all starts and ends within this interval
        # also look at all ends with start < current end past the
        nid_set = set()
        max_so_far = - math.inf
        for n in self.nodes:
            v, starts_set, ends_set = n
            nid_set |= starts_set
            nid_set -= ends_set
            max_so_far = max(max_so_far, len(nid_set))
        return max_so_far


if __name__ == '__main__':
    mt = MyCalendarThree()
    # ["MyCalendarThree","book","book","book","book","book","book","book","book","book","book"]
    # [[],[26,35],[26,32],[25,32],[18,26],[40,45],[19,26],[48,50],[1,6],[46,50],[11,18]]
    #
    #["MyCalendarThree", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book"]
    for val in [[26, 35], [26, 32], [25, 32], [18, 26]]:
        print(mt.book(*val))
