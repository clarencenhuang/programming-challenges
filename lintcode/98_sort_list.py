from lintcode.datastructure_util import ListNode


def quicksort(start, end=None):
    if start == end:
        return start
    dummy = ListNode(-1, start)
    pivot = start
    prev, cur = pivot, pivot.next
    while cur and cur != end:
        ncurr = cur
        if cur.val < pivot.val:
            prev.next = cur.next
            ncurr = prev
            dummy.next, cur.next = cur, dummy.next
        prev, cur = ncurr, ncurr.next

    dummy.next = quicksort(dummy.next, pivot)
    pivot.next = quicksort(pivot.next, end)
    return dummy.next


def merge_sort(start):

    def merge(cur1, cur2):
        dummy = ListNode(-1, start)
        ptr = dummy
        while cur1 or cur2:
            if not cur2 or (cur1 and cur1.val <= cur2.val):
                ptr.next, ptr, cur1 = cur1, cur1, cur1.next
            elif not cur1 or (cur2 and cur2.val <= cur1.val):
                ptr.next, ptr, cur2 = cur2, cur2, cur2.next
        return dummy.next

    def mergesort(s):
        if not s or s.next is None:
            return s
        slow, fast = s, s.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        slow.next, part2 = None, slow.next
        p1 = mergesort(s)
        p2 = mergesort(part2)
        return merge(p1, p2)

    return mergesort(start)





if __name__ == '__main__':
    ls = ListNode.create_from_string('21->25->25->31->4->null')
    #a = quicksort(ls)
    a = merge_sort(ls)
    print(a)