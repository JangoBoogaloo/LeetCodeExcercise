from typing import List
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_nums = deque()
        max_nums = deque()
        left = 0
        for right in range(len(nums)):
            # for a new data nums[right], anything inside its range will be useless
            # we are recording the max range in order,
            # then later we can shrink and get smaller (next biggest) range
            while len(max_nums) and nums[right] > max_nums[-1]:
                max_nums.pop()
            while len(min_nums) and nums[right] < min_nums[-1]:
                min_nums.pop()

            max_nums.append(nums[right])
            min_nums.append(nums[right])

            if max_nums[0] - min_nums[0] > limit:
                # if the left boundary happens to be the range record.
                # we can now remove that range record
                if max_nums[0] == nums[left]:
                    max_nums.popleft()
                if min_nums[0] == nums[left]:
                    min_nums.popleft()
                # we have to shrink window anyway
                left += 1
        return len(nums) - left