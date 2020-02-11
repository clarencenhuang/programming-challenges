from collections import defaultdict

def sum2(arr, k):
    lookup = defaultdict(set)
    for i, n in enumerate(arr):
        lookup[n].add(i)
    for i, n in enumerate(arr):
        diff = k - n
        if diff in lookup:
            for j in lookup[diff]:
                if i != j:
                    return list(sorted([i, j]))
    return []
