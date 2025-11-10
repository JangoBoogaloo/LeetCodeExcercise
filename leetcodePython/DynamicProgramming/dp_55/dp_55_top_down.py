from typing import List

class Solution:
    NotSet = 0
    Succeed = 1
    Fail = 2
    def _canJumpAt(self, start: int, canJumpAt: List[int], nums: List[int]) -> int:
        if canJumpAt[start] != self.NotSet:
            return canJumpAt[start]
        jumpRange = min(start + nums[start], len(nums) - 1)
        for location in range(start+1, jumpRange+1):
            if self._canJumpAt(location, canJumpAt, nums) == self.Succeed:
                canJumpAt[start] = self.Succeed
                return canJumpAt[start]
        canJumpAt[start] = self.Fail
        return canJumpAt[start]

    def canJump(self, nums: List[int]) -> bool:
        canJumpAt = [self.NotSet] * len(nums)
        canJumpAt[-1] = self.Succeed
        return self._canJumpAt(0, canJumpAt, nums) == self.Succeed





