from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_greater = {}
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                nums2_greater[nums2[stack.pop()]] = nums2[i]
            stack.append(i)
        ans = []
        for num in nums1:
            if num in nums2_greater:
                ans.append(nums2_greater[num])
            else:
                ans.append(-1)
        return ans