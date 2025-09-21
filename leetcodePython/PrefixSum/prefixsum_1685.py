from itertools import accumulate
from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefixSum = [0]+list(accumulate(nums))
        answers = []
        for i in range(1, len(nums)+1):
            currSum = prefixSum[-1] - prefixSum[i] - prefixSum[i-1] + (2*i-1 - len(nums)) * nums[i-1]
            answers.append(currSum)
        return answers
