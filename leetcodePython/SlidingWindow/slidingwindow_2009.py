from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        sortedUnique = sorted(set(nums))
        left = 0
        for right in range(1, len(sortedUnique)):
            if sortedUnique[right] - sortedUnique[left] > len(nums) - 1:
                left += 1
        duplicateCount = len(nums) - len(sortedUnique)
        return left + duplicateCount





