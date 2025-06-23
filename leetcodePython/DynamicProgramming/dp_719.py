from typing import List


class Solution:
    def _diffSmallerThan(self, diff: int, nums: List[int]) -> int:
        left = 0
        count = 0
        for right in range(1, len(nums)):
            while left < right and nums[right] - nums[left] >= diff:
                left += 1
            count += right - left
        return count

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        minDist, maxDist = 0, nums[-1] - nums[0]
        answer = 0
        while minDist <= maxDist:
            guessDist = (minDist + maxDist) // 2
            if self._diffSmallerThan(guessDist, nums) >= k:
                maxDist = guessDist - 1
            else:
                answer = guessDist
                minDist = guessDist + 1
        return answer





