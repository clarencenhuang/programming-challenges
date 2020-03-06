

def partition(n, x):
    cur = n
    less_than, greater_than = [], []
    while cur:
        if cur.val < x:
            less_than.append(cur)
        else:
            greater_than.append(cur)
    ls = less_than + greater_than
    for i in range(len(ls)):
        ls[i].next = ls[i+1] if i < len(ls) - 1 else None
    return ls[0] if len(ls) > 0 else n

