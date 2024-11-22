from typing import List


class SolutionReverseDP:
    def canJump(self, nums: List[int]) -> bool:
        BOUNDARY = len(nums) - 1
        SUCCEED, FAILED, UNKNOWN = 1, 0, -1
        pos_finish_status = [UNKNOWN] * (len(nums) - 1)
        pos_finish_status.append(SUCCEED)

        for i in range(len(nums)-2, -1, -1):
            furthest = min(i + nums[i], BOUNDARY)
            for j in range(i+1, furthest + 1):
                if pos_finish_status[j] == SUCCEED:
                    pos_finish_status[i] = SUCCEED
                    break
        return pos_finish_status[0] == SUCCEED
