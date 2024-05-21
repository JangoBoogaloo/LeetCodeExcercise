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
        index_stack = []
        for i in range(2*len(nums)):
            index = i%len(nums)
            while index_stack and nums[index] > nums[index_stack[-1]]:
                res[index_stack.pop()] = nums[index]
            index_stack.append(index)
        return res