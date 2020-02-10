

def partition_array(nums, pivot):
    divider = 0
    for i, n in enumerate(nums):
        if n < pivot:
            nums[i], nums[divider] = nums[divider], nums[i]
            divider += 1
    return divider


if __name__ == '__main__':
    partition_array([9,7,5,4,3,2], 4)


