from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        prefixProduct, suffixProduct = 1, 1
        maxProduct = nums[0]
        for i, num in enumerate(nums):
            if prefixProduct == 0:
                prefixProduct = num
            else:
                prefixProduct *= num

            if suffixProduct == 0:
                suffixProduct = nums[len(nums)-i-1]
            else:
                suffixProduct *= nums[len(nums)-i-1]

            maxProduct = max(maxProduct, prefixProduct, suffixProduct)
        return maxProduct