from typing import List


def get_skyline(buildings: List[List[int]]) -> List[List[int]]:
    coords = list(sorted(list(set([c for l, r, _ in buildings for c in (l, r)]))))
    index = {c: i for i, c in enumerate(coords)}
    heights = [0] * len(coords)
    buildings_sort_h = list(sorted([(h, l, r) for l, r, h in buildings]))
    for h, l, r in buildings_sort_h:
        idx_l = index[l]
        idx_r = index[r]
        print(f"l: {coords[idx_l]} r: {coords[idx_r]}")
        heights[idx_l] = h
        for idx in range(idx_l + 1, idx_r):
            heights[idx] = -1

    skyline = [[None, None]]
    for i, h in enumerate(heights):
        if h == -1 or h == skyline[-1][1]:
            continue
        skyline.append([coords[i], h])
    skyline.pop(0)
    return skyline


if __name__ == '__main__':
    buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    print(get_skyline(buildings))



