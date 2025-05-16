from typing import List


class SolutionAuxiliaryArray:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        # Keeps track of flipped states
        flipped = [False] * len(nums)

        # Tracks valid flips within the past window
        curr_window_flips = 0

        # Counts total flips needed
        flipCount = 0

        for i in range(len(nums)):
            if i >= k:
                # flip out of current window should be excluded
                if flipped[i - k]:
                    curr_window_flips -= 1

            # odd flip means new data will flip, if data is 1, current odd flip will change it to 0, then that means new data needs another flip
            if curr_window_flips % 2 == nums[i]:
                # if we can not isolate to flip this new bit (can't form next k window), we can't get all 1
                if i + k > len(nums):
                    return -1

                curr_window_flips += 1
                flipped[i] = True
                flipCount += 1

        return flipCount


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        total_flips = 0
        current_flips = 0
        for right in range(len(nums)):
            if right >= k and nums[right - k] == 2:
                current_flips -= 1

            # odd flip means new data will flip, if data is 1, current odd flip will change it to 0, then that means new data needs another flip
            if nums[right] == (current_flips % 2):
                if right + k > len(nums):
                    return -1
                # we use 2 to mark that the data is flipped
                nums[right] = 2
                current_flips += 1
                total_flips += 1
        return total_flips


if __name__ == "__main__":
    sol = Solution()
    sol.minKBitFlips([0, 1, 0], 2)
