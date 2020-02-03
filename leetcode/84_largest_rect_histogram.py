from collections import OrderedDict
from typing import List

'''
For every bar ‘x’, we calculate the area with ‘x’ as the smallest bar in the rectangle. If we calculate such area for 
every bar ‘x’ and find the maximum of all areas, our task is done. How to calculate area with ‘x’ as smallest bar? 
We need to know index of the first smaller (smaller than ‘x’) bar on left of ‘x’ and index of first smaller bar on 
right of ‘x’. Let us call these indexes as ‘left index’ and ‘right index’ respectively. We traverse all bars from left 
to right, maintain a stack of bars. Every bar is pushed to stack once. A bar is popped from stack when a bar of smaller 
height is seen. When a bar is popped, we calculate the area with the popped bar as smallest bar. How do we get left and 
right indexes of the popped bar – the current index tells us the ‘right index’ and index of previous item in stack 
is the ‘left index’. Following is the complete algorithm.

Create an empty stack.

Push 0 to end of the given bar array. Because bar with height= 0 means lower than any other bars. This ensure everything 
in static will be popped out for calculation.

Loop from right to left,
If stack is empty or bar[i] is higher than bar at top of stack, push index i into stack.
If bar[i] is lower than the top of stack, pop out the top of stack, say it is hist[tp]. Use it as lowest bar. the 
leftIndex is current top of stack. the rightIndex is i.

If the stack is not empty, then one by one remove all bars from stack and do step 2.b for every removed bar. until 
seeing a bar in stack lower than current bar[i]

'''

def stack_solution(heights: List[int]) -> int:
    last_h = 0
    stack = []
    max_area = 0
    for i, h in enumerate(heights):
        if not stack or h >= last_h:
            stack.append(i)
        else:
            while stack and h < heights[stack[-1]]:
                top_i = stack.pop()
                top_h = heights[top_i]
                max_area = max(max_area, (i - top_i) * top_h)
            stack.append(i)
        last_h = h
    if stack:
        max_area = max(max_area, heights[stack[0]] * len(stack))
    return max_area




class Solution:


    '''
    my idea is to look at the bars, wheenever a bigger bar comes
        we keep track of it as a potential start of a bigger rectangle
        whenever a smaller bar comes in, we look over all previous bigger bars and "knock them down" to the smaller size

    The solutions posted in leetcode are much better.
    '''
    def largestRectangleArea(self, heights: List[int]) -> int:
        levels = OrderedDict()
        largest = 0
        ph = 0
        for i, h in enumerate(heights):
            if h > ph:
                levels[i] = h
            if h < ph:
                to_remove = set()
                to_update = {}
                seen = set()
                for idx, level in levels.items():
                    if level > h:
                        area = (i - idx) * level
                        largest = max(largest, area)
                        if h in seen:
                            to_remove.add(idx)
                        else:
                            level = h
                            to_update[idx] = level
                            seen.add(level)
                for key in to_remove:
                    del levels[key]
                for k,v in to_update.items():
                    levels[k] = v
            ph = h
        for i, level in levels.items():
            area = level * (len(heights) - i)
            largest = max(largest, area)
        return largest


if __name__ == '__main__':
    s = Solution()
    #print(s.largestRectangleArea([2,1,5,6,2,3]))
    print(stack_solution([2,1,5,6,2,3]))







