from typing import List
from operator import add, truediv, mul, sub

operators = (add, sub, truediv, mul)
operator2str = {
    add: '+',
    truediv: '/',
    mul: '*',
    sub: '-'
}


class Solution:

    def judgePoint24(self, nums: List[int]) -> bool:
        seen = set()

