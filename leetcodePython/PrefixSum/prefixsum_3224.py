from typing import List


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        changesAtDiff = [0] * (k + 1 + 1)
        changesAtDiff[0] = len(nums) // 2
        print(changesAtDiff)
        for i in range(len(nums) // 2):
            leftNum, rightNum = nums[i], nums[len(nums) - 1 - i]
            diff = abs(leftNum - rightNum)
            maxDiff = max(leftNum, rightNum, k-leftNum, k-rightNum)
            changesAtDiff[diff] -= 1
            changesAtDiff[diff + 1] += 1
            changesAtDiff[maxDiff + 1] += 1

        changes = 0
        minChange = len(nums) // 2
        for diff in range(k+1):
            changes += changesAtDiff[diff]
            minChange = min(minChange, changes)
        return minChange
