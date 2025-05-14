from typing import List
from heapq import heappop, heappush


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        unusedRooms = [i for i in range(n)]
        endtime_usedrooms = []
        roomMeetingsCount = [0] * n
        meetings.sort()
        for start, end in meetings:
            while endtime_usedrooms and start >= endtime_usedrooms[0][0]:
                _, roomId = heappop(endtime_usedrooms)
                heappush(unusedRooms, roomId)
            if unusedRooms:
                roomId = heappop(unusedRooms)
                heappush(endtime_usedrooms, (end, roomId))
            else:
                availableTime, roomId = heappop(endtime_usedrooms)
                duration = end - start
                delayedEndTime = availableTime+duration
                heappush(endtime_usedrooms, (delayedEndTime, roomId))

            roomMeetingsCount[roomId] += 1
        return roomMeetingsCount.index(max(roomMeetingsCount))
