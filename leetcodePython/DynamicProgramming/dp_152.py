from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        prefixProduct, suffixProduct = 1, 1
        maxProduct = nums[0]
        for i in range(len(nums)):
            prefixProduct = nums[i] if prefixProduct == 0 else nums[i] * prefixProduct
            suffixProduct = nums[len(nums) - i - 1] if suffixProduct == 0 else nums[len(nums) - i - 1] * suffixProduct
            maxProduct = max(maxProduct, prefixProduct, suffixProduct)
        return maxProduct


class SolutionBruteForce:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxProduct = nums[0]
        for start in range(len(nums)):
            currProduct = 1
            for end in range(start, len(nums)):
                currProduct += nums[end]
                maxProduct = max(maxProduct, currProduct)
        return maxProduct
