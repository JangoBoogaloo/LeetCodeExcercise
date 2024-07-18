from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # 3:   11
        # 8: 1000
        # if we want something & 3 and & 8 also 0, we need to accumulate those diff bit as 1 bit
        # for any new data, the diff bit should also zero those 1 bit
        accumulate_and = 0
        left = 0
        ans = 0
        for right in range(len(nums)):
            # if the accumulated result & nums shows non-zero
            while accumulate_and & nums[right]:
                # we have to remove the bit from left edge
                accumulate_and = accumulate_and ^ nums[left]
                left += 1
            # count the new 1 bits in accumulated result, using OR
            accumulate_and |= nums[right]
            ans = max(ans, right - left + 1)

        return ans