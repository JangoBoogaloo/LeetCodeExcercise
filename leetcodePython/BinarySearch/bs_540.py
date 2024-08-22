import collections
from typing import List


class SolutionCounter:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        num_count = collections.Counter(nums)

        for key in num_count:
            if num_count[key] == 1:
                return key
        return -1


class SolutionBS:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid_even = (left + right) // 2
            if mid_even % 2 == 1:
                mid_even -= 1

            # 1,1,2,3,3
            # num[0] == num[1], the array before mid_even is good
            if nums[mid_even] == nums[mid_even + 1]:
                left = mid_even + 2
            else:
                right = mid_even

        return nums[left]
