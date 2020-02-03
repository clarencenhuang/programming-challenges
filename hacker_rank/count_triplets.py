from collections import defaultdict
import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

def countTriplets(arr, r):
    val2idx = defaultdict(set)
    q = []
    for i, v in enumerate(arr):
        if v not in val2idx:
            q.append(v)
        val2idx[v].add(i)
    counts = 0
    for v in q:
        if r == 1:
            return ncr(len(val2idx[v]), 3)
        else:
            vr = int(v*r)
            vrr = int(vr*r)
            if vr in val2idx and vrr in val2idx:
                counts += len(val2idx[v]) * len(val2idx[vr]) * len(val2idx[vrr])
    return counts







if __name__ == '__main__':
    arr = [1, 3, 9, 9, 27, 81]
    r = 3
    print(countTriplets([1237] * 100000, 1))