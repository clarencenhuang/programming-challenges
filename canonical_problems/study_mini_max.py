

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @property
    def is_leaf(self):
        return (self.left, self.right) == (None, None)


tree = Node(val=None,
            left=Node(val=None,
                      left=Node(3),
                      right=Node(5)
                      ),
            right=Node(val=None,
                       left=Node(2),
                       right=Node(9)
                       )
            )


def tree_minimax(node: Node, maxturn=True):
    if node.is_leaf:
        return node.val
    if maxturn:
        return max(tree_minimax(node.left, False), tree_minimax(node.right, False))
    else:
        return min(tree_minimax(node.left, True), tree_minimax(node.right, True))

print(tree_minimax(tree, True))