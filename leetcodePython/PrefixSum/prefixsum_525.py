from typing import List


class SolutionBruteForce:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        for left in range(len(nums)):
            ones = zeros = 0
            for right in range(left, len(nums)):
                if nums[right] == 1:
                    ones += 1
                else:
                    zeros +=1
                if zeros == ones:
                    max_len = max(max_len, right - left + 1)
        return max_len


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        one_zero_diff = 0
        max_len = 0
        one_zero_diff_index_map = {0: -1}
        for i, num in enumerate(nums):
            if num == 1:
                one_zero_diff += 1
            else:
                one_zero_diff -= 1
            if one_zero_diff in one_zero_diff_index_map:
                max_len = max(max_len, i - one_zero_diff_index_map[one_zero_diff])
            else:
                one_zero_diff_index_map[one_zero_diff] = i
        return max_len
