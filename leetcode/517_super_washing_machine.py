from collections import defaultdict, deque
from typing import List
from itertools import accumulate

def inefficient(machines):
    total = sum(machines)
    if total % len(machines) != 0:
        return -1
    per_machine = total // len(machines)
    level_table = list(accumulate([per_machine] * len(machines)))
    moves = 0
    while len(set(machines)) > 1:
        cur_sum = 0
        moved = set()
        for i, level in enumerate(level_table):
            if i == len(level_table) - 1:
                break
            cur_sum += machines[i]
            if cur_sum < level and machines[i + 1] > 0 and (i + 1) not in moved:
                cur_sum += 1
                machines[i] += 1
                machines[i + 1] -= 1
                moved.add(i + 1)
            elif cur_sum > level and machines[i] > 0 and i not in moved:
                cur_sum -= 1
                machines[i] -= 1
                machines[i + 1] += 1
                moved.add(i)
        moves += 1
    return moves



class Solution:

    ''' each turn we can move 1 unit across many machines, we calculate at each machine, how many moves it will take
     to reach equilibrium

     '''
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        n = len(machines)
        if total % n != 0:
            return -1
        avg = total // n
        sum_table = [0] + list(accumulate(machines))
        moves = 0
        for i in range(n):
            left_amt =  sum_table[i] - avg * i
            right_amt = (sum_table[n] - sum_table[i + 1]) - avg * (n - i - 1)
            if left_amt > 0 and right_amt > 0: # both needs to transport to me
                moves = max(moves, left_amt, right_amt)
            elif left_amt < 0 and right_amt < 0: # i need to transport out to both ppl
                moves = max(moves, abs(left_amt) + abs(right_amt))
            else:
                moves = max(moves, abs(left_amt), abs(right_amt)) # max amount out of equilibrium that needs to be transported, take max
        return moves






if __name__ == '__main__':
    s = Solution()
    a = [70245,77822,7921,1696,32988,37651,1,83166,87173,49392,98685,48950,50583,96901,74270,3311,51937,95628,96270,41493,39529,25251,64928,51521,5389,49035,64882,32584,39051,44316,31435,36445,15868,76835,80931,92547,54907,71705,33945,90291,86275,84865,54020,31975,82838,64029,28304,17281,90970,39213,95015,64762,55453,63014,3404,77131,1466,6411,5576,63345,52692,28875,8027,94433,90719,69686,22804,53896,91518,30173,56572,15069,97510,75077,71980,26566,75522,74888,27039,56868,47952,29768,8801,35932,20136,10320,55399,51138,8189,63722,52729,6980,39036,45622,83530,79184,84754,95854,88840,91875]
    print(s.findMinMoves(a))



