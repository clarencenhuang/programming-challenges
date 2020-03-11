from lintcode.datastructure_util import TreeNode, ListNode


def ll_to_bin_tree(start):
    cur = start
    arr = []
    while cur:
        arr.append(cur)
        cur = cur.next

    def maketree(arr):
        if len(arr) == 0:
            return None
        m = len(arr) // 2
        tr = TreeNode(arr[m].val)
        tr.left = maketree(arr[:m])
        tr.right = maketree(arr[m+1:])
        return tr

    return maketree(arr)

if __name__ == '__main__':
    ls = ListNode.create_from_string('2->3->6->7')
    t = ll_to_bin_tree(ls)
    print('b')