'''
top down DP formulation

dp[i] = (sorted list of chips to cover up to i)

dp[i] = if dp[i-1] cover up to dp [i]
    otherwise dp[i-1] + clip with the latest ending
'''
import bisect
import math
import functools

def video_stiching(clips, t):
    clips = list(sorted(clips)) # sort by start time

    @functools.lru_cache(None)
    def dp(i):
        if i == 0:
            last_end = [-1, 0]
            prev = []
        else:
            prev = dp(i - 1)
            if prev is None:
                return None
            last_end = prev[-1]
            if last_end[1] >= i:
                return prev
        max_clip = [0, 0]
        idx_start = bisect.bisect(clips, last_end)
        idx_end = bisect.bisect(clips, [i, math.inf])
        for k in range(idx_start, idx_end):
            if clips[k][0] <= last_end[1] and clips[k][1] > max_clip[1]:
                max_clip = clips[k]
        if max_clip == [0, 0]:
            return None
        return prev + [max_clip]

    res = dp(t)
    if not res:
        return -1
    else:
        if res[-1][1] < t:
            return -1
        return len(res)

if __name__ == '__main__':
    print(video_stiching([[0,5],[1,6],[2,7],[3,8],[4,9],[5,10],[6,11],[7,12],[8,13],[9,14],[10,15],[11,16],[12,17],[13,18],[14,19],[15,20],[16,21],[17,22],[18,23],[19,24],[20,25],[21,26],[22,27],[23,28],[24,29],[25,30],[26,31],[27,32],[28,33],[29,34],[30,35],[31,36],[32,37],[33,38],[34,39],[35,40],[36,41],[37,42],[38,43],[39,44],[40,45],[41,46],[42,47],[43,48],[44,49],[45,50],[46,51],[47,52],[48,53],[49,54]], 50))