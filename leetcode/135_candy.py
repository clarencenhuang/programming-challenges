# https://leetcode.com/problems/candy/
'''
thought process

each candy candy[i], the miminum amount for this guy is the max( rising_edge_left, falling_edge_right)

rising_edge_left[i] = if candy[i] > candy[i-1]: 1 + rising_edge_left[i-1] else: 0
falling_edge_right[i] = if candy[i] > candy[i+1]: 1 + falling_edge_right[i+1] else: 0

'''


def min_amt(candy):
    rising_edge_left = [0] * len(candy)
    falling_edge_right = [0] * len(candy)
    for i in range(1, len(candy)):
        if candy[i] > candy[i-1]:
            rising_edge_left[i] = rising_edge_left[i-1] + 1
    for i in range(len(candy) - 2, -1, -1):
        if candy[i] > candy[i+1]:
            falling_edge_right[i] = falling_edge_right[i+1] + 1
    num_candy = 0
    for i in range(len(candy)):
        num_candy += max(rising_edge_left[i], falling_edge_right[i]) + 1
    return num_candy

if __name__ == '__main__':
    print(min_amt([1,2,3,3,2,1]))