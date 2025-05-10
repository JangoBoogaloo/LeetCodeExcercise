from typing import List


class Solution:
    def _threeSumStartFromIndex(self, nums: List[int], index: int, target: int, result: List[List[int]]):
        left = index + 1
        right = len(nums) - 1
        while left < right:
            currSum = nums[index] + nums[left] + nums[right]
            if currSum > target:
                right -= 1
            elif currSum < target:
                left += 1
            else:
                result.append([nums[index], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self._threeSumStartFromIndex(nums, i, 0, result)
        return result