from collections import defaultdict
import math

def count_sol_solution(a, k):
    freq_table = defaultdict(lambda: 0)
    freq_table[0] = 1
    cursum = 0
    counts = 0
    mini, maxi = 0, 0
    for n in a:
        cursum += n
        mini, maxi = min(cursum, mini), max(cursum, maxi)
        mintry, maxtry = cursum - maxi, cursum - mini
        min_i, max_i = mintry // k, maxtry // k
        for i in range(min_i, max_i + 1):
            to_sub = i * k
            diff = cursum - to_sub
            if diff in freq_table:
                counts += freq_table[diff]
        freq_table[cursum] += 1
    return counts


if __name__ == "__main__":
    a = [-5] #[4,5,0,-2,-3,1]
    k = 5
    print(count_sol_solution(a, k))