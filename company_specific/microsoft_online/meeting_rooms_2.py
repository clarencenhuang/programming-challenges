# https://www.lintcode.com/problem/meeting-rooms-ii/description
import heapq


def num_meeting_rooms(meetings):
    meetings = sorted(meetings)
    meeeting_ends = []
    num_rooms = 0
    for start, end in meetings:
        if meeeting_ends and meeeting_ends[0] <= start:
            heapq.heappop(meeeting_ends)
        else:
            num_rooms += 1
        heapq.heappush(meeeting_ends, end)
    return num_rooms


if __name__ == '__main__':
    assert num_meeting_rooms([(0,30),(5,10),(15,20)]) == 2
    assert num_meeting_rooms([(2,7)]) == 1