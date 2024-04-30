from typing import List


class Solution:
    def _substringMaxMatch(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        for i in range(len(nums1)):
            consecutive_match = 0
            for (n1, n2) in zip(nums1[i:], nums2):
                if n1 == n2:
                    consecutive_match += 1
                else:
                    res = max(res, consecutive_match)
                    consecutive_match = 0
            res = max(res, consecutive_match)
        return res

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        return max(self._substringMaxMatch(nums1, nums2), self._substringMaxMatch(nums2, nums1))
