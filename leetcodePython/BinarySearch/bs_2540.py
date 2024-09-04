import bisect
from typing import List


class SolutionBS:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        for num in nums1:
            idx = bisect.bisect_left(nums2, num)
            if idx < len(nums2) and nums2[idx] == num:
                return num
        return -1


class SolutionTwoPointers:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        index_1, index_2 = 0, 0
        while index_1 < len(nums1) and index_2 < len(nums2):
            if nums1[index_1] < nums2[index_2]:
                index_1 += 1
            elif nums1[index_1] > nums2[index_2]:
                index_2 += 1
            else:
                return nums1[index_1]
        return -1
