from typing import List
from heapq import  heappush, heappop
from collections import defaultdict
import math

def smallest_range(nums: List[List[int]]) -> List[int]:
    merged = []
    heap = []
    num_lists = len(nums)
    # merge the k lists using a heap
    for i, ls in enumerate(nums):
        heappush(heap, (ls.pop(0), i))
    while heap:
        num, i = heappop(heap)
        merged.append((num, i))
        if len(nums[i]) > 0:
            heappush(heap, (nums[i].pop(0), i))

    # use 2 pointers to form a sliding window
    ptr0 = 0
    idx_window = defaultdict(lambda: 0)
    min_window, min_win_n0 = math.inf, math.inf
    for ptr1, (_, list_i) in enumerate(merged):
        idx_window[list_i] += 1
        while len(idx_window) == num_lists:
            n0, n1 = merged[ptr0][0], merged[ptr1][0]
            win_len = n1 - n0
            if win_len < min_window or (win_len == min_window and n0 < min_win_n0):
                min_window = win_len
                min_win_n0 = n0
            to_remove = merged[ptr0][1]
            idx_window[to_remove] -= 1
            if idx_window[to_remove] == 0:
                del idx_window[to_remove]
            ptr0 += 1

    return [min_win_n0, min_win_n0 + min_window]

if __name__ == '__main__':
    lists = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
    print(smallest_range(lists))