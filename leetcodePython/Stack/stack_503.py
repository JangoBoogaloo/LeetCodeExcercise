from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        greater = [-1] * len(nums)
        decreaseNumIndex = []
        for i in range(len(nums)*2):
            index = i % len(nums)
            while decreaseNumIndex and nums[index] > nums[decreaseNumIndex[-1]]:
                greater[decreaseNumIndex.pop()] = nums[index]
            decreaseNumIndex.append(index)
        return greater
