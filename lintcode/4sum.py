# https://www.lintcode.com/problem/4sum/description?_from=ladder&&fromId=2
import itertools
import collections



def sum4(numbers, target):
    numbers = sorted(numbers)
    sum2 = collections.defaultdict(set)
    target_nums = set()
    for i, num in enumerate(numbers):
        for j, num2 in itertools.islice(enumerate(numbers), i + 1, None):
            sum2[num + num2].add(frozenset({i, j}))

    for s2, indices in sum2.items():
        rem = target - s2
        if rem in sum2:
            other_indices = sum2[rem]
            for i1, i2 in itertools.product(indices, other_indices):
                idx_set = i1 | i2
                if len(idx_set) == 4:
                    target_nums.add(tuple(sorted([numbers[i] for i in idx_set])))
    return list(map(list, target_nums))

if __name__ == '__main__':
    # print(sum4([1,0,-1,0,-2,2], 0))
    # print(sum4([1,0,-1,0,-2,2], -2))
    print(fourSum([1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,0,0,-2,2,-5,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99], 11))