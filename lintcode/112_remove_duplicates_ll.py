def remove_duplicates(n):
    cur = n
    while cur:
        nex = cur.next
        while nex and nex.val == cur.val:
            nex = nex.next
        cur.next = nex
    return n
