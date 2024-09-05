from typing import List


class Solution:
    def _count_pair_with_max_distance(self, nums: List[int], distance: int) -> int:
        left = 0
        count = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > distance:
                left += 1
            count += right - left
        return count

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        left = 0
        right = nums[-1] - nums[0]
        while left < right:
            guess_distance = (left + right) // 2
            count = self._count_pair_with_max_distance(nums, guess_distance)
            if count < k:
                left = guess_distance + 1
            else:
                right = guess_distance
        return left
