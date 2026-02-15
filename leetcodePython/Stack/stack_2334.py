from typing import List


class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        stack = []
        leftBoundFor = [i for i in range(len(nums))]
        for i in range(len(nums)):
            num = nums[i]
            # 3, 2, 1
            while stack and num <= nums[stack[-1]]:
                leftBoundFor[i] = leftBoundFor[stack.pop()]
            stack.append(i)

        stack = []
        rightBoundFor = [i for i in range(len(nums))]
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            # 3, 2, 1
            while stack and num <= nums[stack[-1]]:
                rightBoundFor[i] = rightBoundFor[stack.pop()]
            stack.append(i)

        for i in range(len(nums)):
            k = rightBoundFor[i] - leftBoundFor[i] + 1
            if nums[i] > threshold / k:
                return k
        return -1
