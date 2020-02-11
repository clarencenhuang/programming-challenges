import bisect
import math

def find_subarray(numbers):
    if len(numbers) == 1:
        return [0, 0]
    indices = []
    min_diff = math.inf
    cumsum = 0
    prev_cum_sum = []
    for i, n in enumerate(numbers):
        cumsum += n
        idx = bisect.bisect(prev_cum_sum, (cumsum, i))
        if cumsum == 0:
            indices = [0, i]
            break
        if len(prev_cum_sum) > 0:
            if 0 <= idx <= len(prev_cum_sum) - 1:
                v, j = prev_cum_sum[idx]
                if abs(cumsum - v) < min_diff:
                    min_diff = abs(cumsum - v)
                    indices = [j + 1, i]
            if 0 <= (idx - 1) <= len(prev_cum_sum) - 1:
                v, j = prev_cum_sum[idx - 1]
                if abs(cumsum - v) < min_diff:
                    min_diff = abs(cumsum - v)
                    indices = [j + 1, i]
        prev_cum_sum.insert(idx, (cumsum, i))
    return indices

if __name__ == '__main__':
    print(find_subarray([3,-3,5]))


