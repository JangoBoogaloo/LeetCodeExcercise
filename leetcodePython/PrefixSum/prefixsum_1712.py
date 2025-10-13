from typing import List


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)

        midMin = 0
        midMax = 0
        total = 0
        for left in range(1, len(prefixSum)):
            midMin = max(midMin, left + 1)
            while midMin < len(nums) and prefixSum[midMin] < 2 * prefixSum[left]:
                midMin += 1
            midMax = max(midMax, midMin)
            while midMax < len(nums) and 2 * prefixSum[midMax] <= prefixSum[left] + prefixSum[-1]:
                midMax += 1
            total += midMax - midMin
        return total % 1_000_000_007









