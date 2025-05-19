from typing import List


class Solution:
    @staticmethod
    def reverseAt(start:int, end:int, nums:List[int]) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        if k == 0:
            return
        nums.reverse()
        self.reverseAt(0, k-1, nums)
        self.reverseAt(k, len(nums)-1, nums)