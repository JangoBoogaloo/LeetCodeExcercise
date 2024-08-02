from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # in case the interval start is not already sorted
        intervals.sort(key=lambda x: x[0])
        left = intervals[0][0]
        right = intervals[0][1]
        ans = []
        for i in range(1, len(intervals)):
            if intervals[i][0] > right:
                ans.append([left, right])
                left = intervals[i][0]
            right = max(right, intervals[i][1])
        ans.append([left, right])

        return ans

if __name__ == '__main__':
    sol = Solution()
    a = sol.merge([[1,4],[4,5]])
    print(a)