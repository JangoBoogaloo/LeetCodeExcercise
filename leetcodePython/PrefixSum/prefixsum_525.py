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


class SolutionHashMapPrefix:
    def findMaxLength(self, nums: List[int]) -> int:
        # we calculate how many 1 we get, if we get 0, we get subtract our 1.
        # The goal is to balance between 1 and 0
        max_len = ones = 0

        # using prefix concept, start from very beginning, we record the index and its '1's.
        # when we hit two index with same '1's, that means between these index we build a subarray with zero '1's
        # that means 1 and 0 are balanced
        one_index_map = {0: -1}
        for i, num in enumerate(nums):
            if num == 1:
                ones += 1
            else:
                ones -= 1
            if ones in one_index_map:
                max_len = max(max_len, i-one_index_map[ones])
            else:
                one_index_map[ones] = i
        return max_len
