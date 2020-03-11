from lintcode.datastructure_util import ListNode

def reverse_ll_1pass(n):
    a, b = None, n
    while b:
        b_next = b.next
        b.next = a
        a, b = b, b_next
    return a

if __name__ == '__main__':
    ls = ListNode.create_from_string('1->2->3->4->5->null')
    print(reverse_ll_1pass(ls))