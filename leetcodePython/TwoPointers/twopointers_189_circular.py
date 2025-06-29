from typing import List


class Solution:
    @staticmethod
    def _circularJump(currentIndex, numBeforeSwap, k, nums:List[int]) -> int:
        swapCount = 0
        start = currentIndex
        while True:
            jumpIndex = (currentIndex + k) % len(nums)
            nums[jumpIndex], numBeforeSwap = numBeforeSwap, nums[jumpIndex]
            currentIndex = jumpIndex
            swapCount += 1
            if start == currentIndex:
                break
        return swapCount

    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        if k == 0:
            return
        start = 0
        count = 0
        while count < len(nums):
            count += self._circularJump(start, nums[start], k, nums)
            start += 1





