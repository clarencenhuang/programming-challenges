import math

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def max_path_sum(node: TreeNode):
    if not node:
        return -math.inf, -math.inf
    sum_left_arm, max_left = max_path_sum(node.left)
    sum_right_arm, max_right = max_path_sum(node.right)

    sum_both_arms = sum_left_arm + node.val + sum_right_arm
    max_sum_arm = max(sum_left_arm + node.val, sum_right_arm + node.val, node.val)

    max_sum = max(sum_both_arms, max_left, max_right, max_sum_arm)
    return max_sum_arm, max_sum

if __name__ == '__main__':
    n = TreeNode(-1)
    r  = TreeNode(9)
    n.right = r
    r.left = TreeNode(-6)
    r.right = TreeNode(3)
    print(max(max_path_sum(n)))

