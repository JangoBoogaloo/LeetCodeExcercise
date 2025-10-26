from typing import List
from bisect import bisect_left

class Solution:
    @staticmethod
    def _find(srcNums, dstNums) -> int:
        for num in srcNums:
            idx = bisect_left(dstNums, num)
            if idx < len(dstNums) and dstNums[idx] == num:
                return num
        return -1

    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1[0] == nums2[0]:
            return nums1[0]
        if nums1[0] < nums2[0]:
            return self._find(nums2, nums1)
        else:
            return self._find(nums1, nums2)








