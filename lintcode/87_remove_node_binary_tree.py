from lintcode.datastructure_util import TreeNode

'''
when we delete a node, we want to replace it with:
    - the largest node in the left subtree
    - the smallest node in the right subtree
    
'''
def delete_node(root: TreeNode, val):

    def find_node(n: TreeNode, v, parent=None):
        if v > n.val:
            return find_node(n.right, v, n)
        elif v < n.val:
            return find_node(n.left, v, n)
        else:
            return n, parent

    def find_successor(n: TreeNode, parent=None):
        if not n.left and not n.right:
            return None
        if n.left:
            n = n.left
            while n.right:
                n = n.right
            return n
        elif n.right:
            n = n.right
            while n.left:
                n = n.left
            return n



    node, parent = find_node(val)
    

