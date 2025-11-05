from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        answer = 0
        for start in range(len(nums)):
            currMin, currMax = float("inf"), float("-inf")
            for end in range(start, len(nums)):
                currMin = min(currMin, nums[end])
                currMax = max(currMax, nums[end])
                answer += currMax - currMin
        return answer







