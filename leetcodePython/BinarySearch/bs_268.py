from typing import List


class SolutionGauss:
    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


class SolutionBinarySearch:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < (mid + 1):
                left = mid + 1
            else:
                right = mid - 1
        return left