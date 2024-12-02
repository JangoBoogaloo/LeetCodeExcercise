from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        total_flips = 0
        current_flips = 0
        FLIPPED = 2
        for right in range(len(nums)):
            if right >= k and nums[right - k] == FLIPPED:
                current_flips -= 1
            # odd flip means new data will flip, if data is 1, current odd flip will change it to 0, then that means new data needs another flip
            if nums[right] == (current_flips % 2):
                if right + k > len(nums):
                    return -1
                # we use 2 to mark that the data is flipped
                nums[right] = FLIPPED
                current_flips += 1
                total_flips += 1
        return total_flips
