from typing import Tuple, Optional


def longest_paren_seq(s: str, i1, i2) -> Optional[Tuple[int, int]]:
    if i1 == i2:
        return i1, i2
    if i2 == i1 + 1:
        return 0, -1
    se = (0, -1)
    if s[i1] == '(' and s[i2 - 1] == ')':
        ii1 = i1 + 1
        ii2 = i2 - 1
        l1, l2 = longest_paren_seq(s, ii1, ii2)
        if l1 == ii1 and l2 == ii2:
            se = i1, i2
        else:
            se = l1, l2
    sl = longest_paren_seq(s, i1 + 1, i2)
    sr = longest_paren_seq(s, i1, i2 - 1)
    return max([sl, sr, se], key=lambda x: x[1] - x[0])


if __name__ == '__main__':
    s = '()()((()))))'
    res = longest_paren_seq(s, 0, len(s))
    print(res)