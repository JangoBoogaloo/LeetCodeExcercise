from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        prevMax, prevMin = nums[0], nums[0]
        globalMax = prevMax
        for num in nums[1:]:
            currMax = max(num, prevMax * num, prevMin * num)
            currMin = min(num, prevMax * num, prevMin * num)
            globalMax = max(globalMax, currMax)
            prevMax = currMax
            prevMin = currMin
        return globalMax
