# https://www.lintcode.com/problem/unique-binary-search-trees/description?_from=ladder&&fromId=2
import functools

'''
for n sorted numbers, we can pick any one to be the root of BST tree
if there are 2, we can pick either one, so 2 ways
otherwise, (number of ways on right) * (number of ways on left)
'''

@functools.lru_cache(None)
def uniq_bst(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2
    return sum([uniq_bst(i) * uniq_bst(n - 1 - i) for i in range(0, n)])


if __name__ == '__main__':
    print(uniq_bst(3))