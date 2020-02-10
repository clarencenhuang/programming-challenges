import math

def sum3_closest(numbers, target):
    numbers = sorted(numbers)
    min_diff = math.inf
    closest_sum = math.inf
    for i in range(len(numbers)):
        j = i + 1
        k = len(numbers) - 1
        while k > j:
            sum3 = numbers[i] + numbers[j] + numbers[k]
            diff = abs(sum3 - target)
            if diff < min_diff:
                min_diff = diff
                closest_sum = sum3
            if sum3 > target:
                k -= 1
            elif sum3 < target:
                j += 1
            else:
                return sum3
    return closest_sum


if __name__ == '__main__':
    print(sum3_closest([2,7,11,15], 3))
    print(sum3_closest([-1,2,1,-4], 1))








if __name__ == '__main__':
    pass