from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0] * (n+1)
        diff = [0] * (n+1)
        for start, end, seats in bookings:
            diff[start] += seats
            if end < n:
                diff[end+1] -= seats
        for i in range(1, len(answer)):
            answer[i] = answer[i-1] + diff[i]
        return answer[1:]




