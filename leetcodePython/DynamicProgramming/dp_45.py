from typing import List


class SolutionDP:
    def jump(self, nums: List[int]) -> int:
        least_jumps = [len(nums)] * (len(nums) - 1)
        least_jumps.append(0)
        for revert_i in range(len(nums)-2, -1, -1):
            furthest = min(revert_i + nums[revert_i], len(nums)-1)
            options = least_jumps[revert_i:furthest+1]
            least_jumps[revert_i] = 1 + min(options)
        return least_jumps[0]


class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        step_left = step_right = 0
        while step_right < len(nums) - 1:
            farthest_jump = 0
            for pos in range(step_left, step_right+1):
                farthest_jump = max(farthest_jump, pos + nums[pos])
            step_left = step_right + 1
            step_right = farthest_jump
            steps += 1
        return steps
