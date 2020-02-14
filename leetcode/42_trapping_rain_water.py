
HEIGHT, IDX = [0, 1]
def trap_rain_water(heights):
    stack = []
    total_water = 0
    for i, h in enumerate(heights):
        intermediates = []
        while stack and stack[-1][HEIGHT] <= h:
            prev = stack.pop()
            intermediates.append(prev)



        stack.append((h, i))
    return total_water


if __name__ == '__main__':
    heights = [3, 0, 0, 1, 0, 0, 3]
    print(trap_rain_water(heights))

