import math
from typing import List


class SolutionBruteForce:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = - math.inf
        for left in range(len(nums)):
            curr_sum = 0
            for right in range(left, len(nums)):
                curr_sum += nums[right]
                max_sum = max(max_sum, curr_sum)

        return max_sum


class SolutionDP:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = max_sum = nums[0]
        for num in nums[1:]:
            # do we want to consider history (concat prev sub array)? If adding history is less, we don't consider
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        return max_sum
