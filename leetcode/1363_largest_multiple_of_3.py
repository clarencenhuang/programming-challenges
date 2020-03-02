'''
Given an integer array of digits, return the largest multiple of three that can be formed by concatenating some of the given digits in any order.

Since the answer may not fit in an integer data type, return the answer as a string.

If there is no answer return an empty string.


Example 1:

Input: digits = [8,1,9]
Output: "981"
Example 2:

Input: digits = [8,6,7,1,0]
Output: "8760"
Example 3:

Input: digits = [1]
Output: ""
Example 4:

Input: digits = [0,0,0,0,0,0]
Output: "0"

DP formulation

the largest you can get the entire thing




'''
from functools import lru_cache


def lm_3(digits):
    digits = list(reversed(sorted(digits)))

    ssum = [0] * len(digits)
    csum = 0
    for i in range(len(digits)):
        csum += digits[i]
        ssum[i] = csum

    lru_cache(None)
    def dp(i, sum_so_far=0):
        if (ssum[i] + sum_so_far) % 3 == 0:
            return




def largest_multiple_of_3(digits):
    digits = list(reversed(sorted(digits)))

    lru_cache(None)
    def knapsack(digits, keep=[]):
        if (sum(digits) + sum(keep)) % 3 == 0:
            return digits + keep
        if len(digits) == 0:
            return []
        smallest = digits[-1]
        # we either remove it, or we keep it
        res = knapsack(digits[:-1], keep)
        res1 = knapsack(digits[:-1], [smallest] + keep)
        if len(res) > len(res1):
            return res
        elif len(res1) > len(res):
            return res1
        else:
            return max(res, res1)

    sack = knapsack(digits)
    if len(sack) > 0:
        return str(int(''.join(map(str, sack))))
    else:
        return ''

if __name__ == '__main__':
    print(largest_multiple_of_3([8,1,9]))
    print(largest_multiple_of_3([8,6,7,1,0]))
    print(largest_multiple_of_3([0,0,0,0,0]))
