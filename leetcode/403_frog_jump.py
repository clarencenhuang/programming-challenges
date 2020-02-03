from collections import defaultdict


# This gets a TLE
def can_cross(stones):
    dp = {(0, 0): True}
    for i in range(1, len(stones)):
        cur_val = stones[i]
        for j in range(0, i):
            prev_val = stones[j]
            gap = cur_val - prev_val
            gaps = [gap - 1, gap, gap + 1]

            for g in gaps:
                if dp.get((j, g), False):
                    print(f'can jump from [{j}:{prev_val}] to [{i}:{cur_val}] with gap of {gap}')
                    dp[(i, gap)] = True
                    if i == len(stones) - 1:
                        return True
                    break
    return False

def can_cross_opt(stones):
    gap_cache = defaultdict(set)
    gap_cache[0].add(1)
    for i in range(1, len(stones)):
        cur_val = stones[i]
        for j in range(0, i):
            prev_val = stones[j]
            gap = cur_val - prev_val
            if gap in gap_cache[j]:
                print(f'can jump from [{j}:{prev_val}] to [{i}:{cur_val}] with gap of {gap}')
                gap_cache[i].add(gap)
                gap_cache[i].add(gap + 1)
                gap_cache[i].add(gap - 1)
                if i == len(stones) - 1:
                    return True

    return False


if __name__ == '__main__':
    print(can_cross_opt([0,1,3,5,6,8,12,17]))