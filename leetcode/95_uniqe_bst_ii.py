'''
any sorted string,


when there is 1 node, there is 1 config

we can pick any node to be root, then rest go left or right

def find_config():
for i,root in ls:
    nodes before root

'''

from lintcode.datastructure_util import TreeNode

import itertools
from functools import lru_cache

def uniq_bst_ii(n):
    @lru_cache(None)
    def bst(nums):
        if len(nums) == 0:
            return [None]
        combos = []
        for i, num in enumerate(nums):
            for left, right in itertools.product(bst(nums[:i]), bst(nums[i+1:])):
                v = TreeNode(nums[i], left=left, right=right)
                combos.append(v)
        return combos
    if n == 0:
        return []
    return bst(tuple(range(1, n+1)))

if __name__ == '__main__':
    print(uniq_bst_ii(0))
