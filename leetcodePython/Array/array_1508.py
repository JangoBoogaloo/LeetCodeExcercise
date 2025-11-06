from typing import List


class Solution:
    _MOD = 10 ** 9 + 7
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sumArrays = [0]
        for start in range(0, len(nums)):
            for end in range(start, len(nums)):
                currSum = sum(nums[start:end+1])
                sumArrays.append(currSum)
        sumArrays.sort()
        return sum(sumArrays[left:right+1]) % self._MOD





