from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = []
        for i, num in enumerate(nums):
            j = (i + 1) % len(nums)
            greater = -1
            while j != i:
                if nums[j] > num:
                    greater = nums[j]
                    break
                j = (j + 1) % len(nums)
            ans.append(greater)
        return ans

class SolutionMonotonicStack:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []
        for i in range(2*len(nums)):
            index = i%len(nums)
            while stack and nums[index] > nums[stack[-1]]:
                res[stack.pop()] = nums[index]
            stack.append(index)
        return res