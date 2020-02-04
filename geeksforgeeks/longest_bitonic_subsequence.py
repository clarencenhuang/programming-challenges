from itertools import islice
from operator import gt, lt

def lis(seq_numbers, op):
    dp = [[i] for i in seq_numbers]
    for i in range(1, len(dp)):
        num = seq_numbers[i]

        for j in range(i - 1, -1, -1):
            pnum = seq_numbers[j]
            if op(num, pnum):
                ls = list(dp[j])
                
    return start_ends


def bitonic_seq(seq_numbers):
    increasing = lis(seq_numbers, gt)
    decreasing = lis(seq_numbers, lt)
    return increasing, decreasing


if __name__ == '__main__':
    seq_numbers = [1, 11, 2, 10, 4, 5, 2, 1]
    print(bitonic_seq(seq_numbers))