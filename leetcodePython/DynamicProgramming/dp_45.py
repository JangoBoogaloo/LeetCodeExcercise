from typing import List


class SolutionDP:
    def jump(self, nums: List[int]) -> int:
        # [3,2,1,1,2,3]
        least_jumps = [len(nums)] * (len(nums) - 1)
        least_jumps.append(0)
        for revert_i in range(len(nums)-2, -1, -1):
            furthest = min(revert_i + nums[revert_i], len(nums)-1)
            options = least_jumps[revert_i:furthest+1]
            least_jumps[revert_i] = 1 + min(options)
        return least_jumps[0]


class Solution:
    def jump(self, nums: List[int]) -> int:
        