from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insert_left, insert_right = newInterval[0], newInterval[1]
        ans = []
        i = 0
        while i < len(intervals):
            if intervals[i][1] >= insert_left:
                insert_left = min(insert_left, intervals[i][0])
                break
            ans.append(intervals[i])
            i += 1

        while i < len(intervals):
            if intervals[i][0] > insert_right:
                break
            insert_right = max(intervals[i][1], insert_right)
            i += 1

        ans.append([insert_left, insert_right])

        while i < len(intervals):
            ans.append(intervals[i])
            i += 1

        return ans
