from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self._kSum(nums, target, 0, 4)

    def _kSum(self, sorted_nums: List[int], target: int, start_at: int, k: int) -> List[List[int]]:
        result = []
        if start_at == len(sorted_nums):
            return result

        average = target / k
        if sorted_nums[start_at] > average or sorted_nums[-1] < average:
            return result

        if k == 2:
            return self._twoSum(sorted_nums, start_at, target)

        for i in range(start_at, len(sorted_nums)):
            if i > start_at and sorted_nums[i] == sorted_nums[i-1]:
                continue
            for sub_solution in self._kSum(sorted_nums, target-sorted_nums[i], i+1, k-1):
                a_solution = [sorted_nums[i]] + sub_solution
                result.append(a_solution)
        return result

    @staticmethod
    def _twoSum(sorted_nums: List[int], start_at: int, target) -> List[List[int]]:
        left = start_at
        right = len(sorted_nums) - 1
        result = []
        while left < right:
            curr_sum = sorted_nums[left] + sorted_nums[right]
            if curr_sum > target:
                right -= 1
                continue
            elif curr_sum < target:
                left += 1
                continue
            if right < len(sorted_nums) - 1 and sorted_nums[right] == sorted_nums[right+1]:
                right -= 1
                continue
            if left > start_at and sorted_nums[left] == sorted_nums[left-1]:
                left += 1
                continue
            result.append([sorted_nums[left], sorted_nums[right]])
            left += 1
            right -= 1
        return result
