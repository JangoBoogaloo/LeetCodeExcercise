from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        maxVal = max(nums)
        frequency = [0] * (maxVal + len(nums))
        for num in nums:
            frequency[num] += 1

        operations = 0
        for i in range(len(frequency)):
            if frequency[i] <= 1:
                continue
            duplicateCount = frequency[i] - 1
            frequency[i + 1] += duplicateCount
            frequency[i] = 1
            operations += duplicateCount
        return operations




