# this was done as a part of the hackerrank timed test for certification

from collections import defaultdict

def most_balanced_partition(parent, file_size):

    tree_size = {}
    children_map = defaultdict(set)
    root = None

    for node, parent  in enumerate(parent):
        if parent == -1:
            root = node
            continue
        children_map[parent].add(node)

    def compute_size(n):
        children_size = 0
        for c in children_map[n]:
            children_size += compute_size(c)
        tree_size[n] = file_size[n] + children_size
        return tree_size[n]

    compute_size(root)

    def do_partition(n, leftover=0):
        # find cutting point where
        # (branch_val) closest_to (node_val - branch_val + leftover)
        my_size = tree_size[n]
        min_diff = abs(my_size - leftover)
        if min_diff == 0:
            return 0
        for cut_at in children_map[n]:
            branch_val = tree_size[cut_at] # this is where we walk down
            other_val = leftover + my_size - branch_val # this is what we leave behind
            if branch_val > other_val:
                # this branch still has something to give
                min_diff = min(min_diff, do_partition(cut_at, other_val))
            else:
                min_diff = min(min_diff, abs(branch_val - other_val))
        return min_diff

    return do_partition(root)

if __name__ == '__main__':
    parent = [-1, 0, 1, 2]
    file_size = [1,4,3,4]
    print(most_balanced_partition(parent, file_size))
    parent = [-1, 0, 0, 0]
    file_size = [10, 11, 10, 10]
    print(most_balanced_partition(parent, file_size))