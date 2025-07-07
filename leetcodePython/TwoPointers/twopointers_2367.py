from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        for left in range(len(nums)):
            num = nums[left]
            mid = self._bsFind(left+1, num+diff, nums)
            if mid < 0:
                continue
            num = nums[mid]
            right = self._bsFind(mid+1, num+diff, nums)
            if right < 0:
                continue
            count += 1
        return count

    @staticmethod
    def _bsFind(start, target, nums:List[int]) -> int:
        left, right = start, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
