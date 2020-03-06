

def rotate_list(n, k):
    ls = []
    cur = n
    while cur:
        ls.append(cur)
        cur = cur.next
    idx = k % len(n)
    ls = ls[-k:] + ls[:-k]
    for i in range(len(ls)):
        ls[i].next = ls[i+1] if i < len(ls) - 1 else None
    return ls[0] if len(ls) > 0 else n