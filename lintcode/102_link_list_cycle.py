
def detect_cycle(l):
    if l is None:
        return False
    slow, fast = l, l.next
    while fast and fast.next:
        if slow == fast:
            return True
        slow, fast = slow.next, fast.next.next
    return False
