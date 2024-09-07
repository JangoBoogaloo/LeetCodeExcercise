from bisect import bisect_left, bisect_right
from typing import List


class SolutionBS:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = bisect_left(nums, target)
        if start == len(nums):
            return [-1, -1]
        end = bisect_right(nums, target) - 1
        if end == -1:
            return [-1, -1]
        if nums[start] != target or nums[end] != target:
            return [-1, -1]
        return [start, end]


if __name__ == "__main__":
    sol = SolutionBS()
    ans = sol.searchRange([5,7,7,8,8,10], 6)
    print(ans)