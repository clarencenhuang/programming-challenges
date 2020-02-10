def sum3zero(numbers):
    numbers = list(sorted(numbers))
    triplets = set()
    for i, n in enumerate(numbers):
        j = i + 1
        k = len(numbers) - 1
        while k > j:
            sum3 = n + numbers[j] + numbers[k]
            if sum3 == 0:
                triplets.add(tuple(sorted([numbers[j], numbers[k], n])))
                k -= 1
                j += 1
            elif sum3 > 0:
                k -= 1
            elif sum3 < 0:
                j += 1
    return list(map(list, triplets))

if __name__ == '__main__':
    print(sum3zero([-1,0,1,2,-1,-4]))
