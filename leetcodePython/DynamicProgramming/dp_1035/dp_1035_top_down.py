from typing import List


class Solution:
    def _maxSubSeqStartAt(self, i1: int, nums1: List[int], i2:int, nums2: List[int], subseqLengthAt):
        if i1 == len(nums1) or i2 == len(nums2):
            return 0
        if i1 in subseqLengthAt and i2 in subseqLengthAt[i1]:
            return subseqLengthAt[i1][i2]
        if i1 not in subseqLengthAt:
            subseqLengthAt[i1] = {}
        if nums1[i1] == nums2[i2]:
            subseqLengthAt[i1][i2] = 1 + self._maxSubSeqStartAt(i1+1, nums1, i2+1, nums2, subseqLengthAt)
        else:
            subseqLengthAt[i1][i2] = max(self._maxSubSeqStartAt(i1+1, nums1, i2, nums2, subseqLengthAt), self._maxSubSeqStartAt(i1, nums1, i2+1, nums2, subseqLengthAt))
        return subseqLengthAt[i1][i2]

    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        subseqLengthAt = {}
        return self._maxSubSeqStartAt(0, nums1, 0, nums2, subseqLengthAt)







