from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_greater = {}
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                nums2_greater[stack.pop()] = num
            stack.append(num)
        ans = []
        for num in nums1:
            if num in nums2_greater:
                ans.append(nums2_greater[num])
            else:
                ans.append(-1)
        return ans