'''
ways to put parenthesis around things

(a, b), c
a, (b, c)


(a, b, c), d
(a, b), (c, d)
a, (b, c, d)

dp(i, j) => results you can get from i, j
dp(i, j) => cross( operator( dp(i, k-1), dp(k+1, j) )  for k from i to j


'''
import re
import functools
from itertools import product
from operator import mul, add, sub, truediv

OPERATOR_MAP = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}


def different_ways(equation):
    numbers = list(map(int, re.split('[-+*/]', equation)))
    operators = [OPERATOR_MAP[o.strip()] for o in re.split('\\d', equation) if len(o) > 0]

    @functools.lru_cache(None)
    def results(i, j):
        if i == j:
            return [numbers[i]]
        if j == i + 1:
            return [operators[i](numbers[i], numbers[j])]
        res = []
        for k in range(i, j):
            p1 = results(i, k)
            p2 = results(k+1, j)
            for n1, n2 in product(p1, p2):
                res.append(operators[k](n1, n2))
        return res

    return list(sorted(results(0, len(numbers) - 1)))


if __name__ == '__main__':
    print(different_ways("2*3-4*5"))