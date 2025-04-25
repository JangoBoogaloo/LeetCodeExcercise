from typing import List


class Solution:
    @staticmethod
    def _maxSubseqWitDigits(nums: List[int], digits: int) -> List[int]:
        removals = len(nums) - digits
        if removals <= 0:
            return nums
        decreaseStack = []
        for num in nums:
            while decreaseStack and removals and decreaseStack[-1] < num:
                decreaseStack.pop()
                removals -= 1
            decreaseStack.append(num)
        if removals:
            decreaseStack = decreaseStack[:-removals]
        return decreaseStack

    @staticmethod
    def _maxMerge(nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1:
            return nums2
        if not nums2:
            return nums1
        index1, index2 = 0, 0
        nums = []
        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1:] > nums2[index2:]:
                nums.append(nums1[index1])
                index1 += 1
            else:
                nums.append(nums2[index2])
                index2 += 1
        if index1 < len(nums1):
            nums.extend(nums1[index1:])
        else:
            nums.extend(nums2[index2:])
        return nums

    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        maxList = []
        for countFrom1 in range(k + 1):
            countFrom2 = k - countFrom1
            if countFrom1 <= len(nums1) and countFrom2 <= len(nums2):
                largest1 = self._maxSubseqWitDigits(nums1, countFrom1)
                largest2 = self._maxSubseqWitDigits(nums2, countFrom2)
                currentMax = self._maxMerge(largest1, largest2)
                maxList = max(maxList, currentMax)
        return maxList




