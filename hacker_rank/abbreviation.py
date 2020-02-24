# https://www.hackerrank.com/challenges/abbr/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming

import functools

def abbr(a, b):

    postfix = [''] * len(a)
    for i in range(len(a) - 1, -1, -1):
        pf_i_plus_1 = '' if i == len(a) - 1 else postfix[i+1]
        if a[i] != a[i].upper():
            postfix[i] = pf_i_plus_1
        else:
            postfix[i] = a[i] + pf_i_plus_1

    def can_xform(i, j):
        if i == len(a) and j == len(b):
            return True
        if a[i].upper() == b[j]:
            return can_xform(i+1, j+1)

if __name__ == '__main__':
    abbr('DFDdsdfDD', '')

