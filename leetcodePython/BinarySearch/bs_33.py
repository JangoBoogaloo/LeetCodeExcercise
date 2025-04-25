from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        if len(nums) < 2:
            if nums[0] == target:
                return 0
            return -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        k = left
        print(k)
        if target >= nums[0]:
            left = 0
            if k == 0:
                right = len(nums) - 1
            else:
                right = k - 1
        else:
            left, right = k, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
