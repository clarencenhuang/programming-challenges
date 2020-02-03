import math
from bisect import bisect
from typing import List
from collections import defaultdict
import itertools


def falling_squares_naive(positions):
    heights = [0] * len(positions)
    max_so_far = 0
    maxes = []
    for i, (left, length) in enumerate(positions):
        x0, x1 = left, left + length
        heights[i] += length
        for j, (left1, length1) in itertools.islice(enumerate(positions), i + 1, None):
            xn0, xn1 = left1, left1 + length1
            if xn0 < x1 and xn1 > x0:
                heights[j] = max(heights[j], heights[i])
        max_so_far = max(max_so_far, heights[i])
        maxes.append(max_so_far)
    return maxes



def falling_squares_direct_index_compression(positions):
    coords = []
    for left, side in positions:
        coords.append(left)
        coords.append(left + side)
    index = {coord: i for i, coord in enumerate(coords)}
    for i, (left, length) in enumerate(positions):
        pass


class Node:

    def __init__(self, lo, hi, val=0):
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


def falling_squares_interval_tree(positions):
    index = {x: i for i, x in enumerate(sorted([x for l, dis in positions for x in (l, l + dis)]))}
    root = Node(0, (len(positions) * 2) - 1)

    res = []
    for left, side in positions:
        x0, x1 = left, left + side
        h = root.query(index[x0], index[x1])
        # print(f'query {index[x0]}, {index[x1]}: {h} ')
        # print(f'update {index[x0]}, {index[x1]}, {h + side}')
        root.update(index[x0], index[x1], h + side)
        res.append(root.val)
    return res


if __name__ == '__main__':
    positions =  [[6,1],[9,2],[2,4]]#
    positions = [[1,2],[2,3],[6,1]]
    positions = [[2,1],[2,9],[1,8]]
    print(falling_squares_naive(positions))
    print(falling_squares_interval_tree(positions))
