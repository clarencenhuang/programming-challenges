import itertools
import functools


@functools.lru_cache(maxsize=None)
def is_scramble(s1, s2):
    if len(s1) != len(s2):
        return False

    if len(s1) == 1 and len(s2) == 1:
        return s1 == s2

    s1s = []
    s2s = []
    for j in range(1, len(s1)):
        s1s.append((s1[:j], s1[j:]))
        s2s.append((s2[:j], s2[j:]))

    for (l1, r1), (l2, r2) in itertools.product(s1s, s2s):
        if ((is_scramble(l1, l2) and is_scramble(r1, r2)) or
                (is_scramble(l1, r2) and is_scramble(l2, r1))):
            return True
    else:
        return False


if __name__ == '__main__':
    s1 = "abcdefghijklmnopq"
    s2 = "efghijklmnopqcadb"
    print(is_scramble(s1, s2))