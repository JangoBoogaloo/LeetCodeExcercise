from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        currentMax = 0
        if not nums:
            return currentMax
        if len(nums) == 1:
            return nums[0]
        prevPrevMax = 0
        prevMax = nums[0]
        for i in range(1, len(nums)):
            currentMax = max(nums[i]+prevPrevMax, prevMax)
            prevPrevMax = prevMax
            prevMax = currentMax
        return currentMax


class SolutionRecursion:
    def _robMaxGainAt(self, index: int, nums: List[int]) -> int:
        if index < 0:
            return 0
        if index == 0:
            return nums[index]
        return max(nums[index] + self._robMaxGainAt(index-2, nums), self._robMaxGainAt(index-1, nums))

    def rob(self, nums: List[int]) -> int:
        return self._robMaxGainAt(len(nums)-1, nums)


if __name__ == '__main__':
    sol = Solution()
    print(sol.rob([1,2,3,1]))