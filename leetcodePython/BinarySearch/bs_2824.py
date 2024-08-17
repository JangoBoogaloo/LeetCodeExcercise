import bisect
from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            # There is no pairs left that matches the condition
            if nums[i] >= target and nums[i] > 0:
                break
            else:
                # find the last index of the second number that matches the condition
                start = i + 1
                end = len(nums) - 1
                mid = 0
                while start <= end:
                    mid = (start + end) // 2
                    if nums[mid] >= target - nums[i]:
                        end = mid - 1
                    else:  # nums[mid] < target - nums[i]
                        start = mid + 1

                res += end - i

        return res
