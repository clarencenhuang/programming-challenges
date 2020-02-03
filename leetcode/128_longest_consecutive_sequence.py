from collections import defaultdict

def longest_consecutive_sequence(nums):
    counts = defaultdict(lambda: 0)
    repeat_remover = set()
    max_counts = 0
    for n in nums:
        if n in repeat_remover:
            continue
        repeat_remover.add(n)
        worth = 1
        if n - 1 in counts:
            worth += counts[n - 1]
        if n + 1 in counts:
            worth += counts[n + 1]
        counts[n] = worth
        if n - 1 in counts:
            l_worth = counts[n - 1]
            counts[n - l_worth] = worth
        if n + 1 in counts:
            r_worth = counts[n + 1]
            counts[n + r_worth] = worth
        max_counts = max(max_counts, worth)
    return max_counts


if __name__ == '__main__':
    arr = [100, 4, 200, 1, 3, 2, 0, 7, 90, 5, 34, 6]
    print(longest_consecutive_sequence(arr))