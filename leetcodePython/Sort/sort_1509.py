import heapq
from typing import List


class SolutionSortGreedy:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()
        min_diff = float('inf')
        '''
        Removing the three largest elements.
        Removing the two largest and one smallest elements.
        Removing one largest and two smallest elements.
        Removing the three smallest elements.
        '''
        for left in range(4):
            right = len(nums) - 4 + left
            curr_diff = nums[right] - nums[left]
            min_diff = min(min_diff, curr_diff)
        return min_diff


class SolutionPartialSortGreedy:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        small_4 = sorted(heapq.nsmallest(4, nums))
        big_4 = sorted(heapq.nlargest(4, nums))

        min_diff = float('inf')
        for i in range(4):
            min_diff = min(min_diff, big_4[i] - small_4[i])
        return min_diff