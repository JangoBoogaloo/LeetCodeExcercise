from typing import List


class Solution:
    def _canSplit(self, nums: List[int], splits: int, sumLimit: int) -> bool:
        currSum = 0
        currentSplit = 1
        for num in nums:
            if currSum + num > sumLimit:
                currSum = 0
                currentSplit += 1
            currSum += num
            if currentSplit > splits:
                return False
        return True

    def splitArray(self, nums: List[int], splits: int) -> int:
        minSum, maxSum = max(nums), sum(nums)
        answerSum = -1
        while minSum <= maxSum:
            guessSum = (minSum + maxSum) // 2
            if self._canSplit(nums, splits, guessSum):
                answerSum = guessSum
                maxSum = guessSum - 1
            else:
                minSum = guessSum + 1
        return answerSum
