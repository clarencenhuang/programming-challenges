
# this is too slow.... look at leetcode solution.
def find_max_3_sum(nums, k):
    iter_range = range(0, len(nums) - k + 1, 1)
    sum1 = {i: sum(nums[i:i + k]) for i in iter_range}
    sum2 = {}
    for j in iter_range:
        for i, val in sum1.items():
            if j >= i + k:
                sum2[(i, j)] = sum1[j] + val
    sum3 = {}
    for l in iter_range:
        for (i, j), val in sum2.items():
            if l >= j + k:
                sum3[i, j, l] = sum1[l] + val
    max_val = max([val for idx, val in sum3.items()])
    idxes = [idx for idx, val in sum3.items() if val == max_val]
    return min(idxes)


if __name__ == '__main__':
    print(find_max_3_sum([1,2,1,2,6,7,5,1], 2))





