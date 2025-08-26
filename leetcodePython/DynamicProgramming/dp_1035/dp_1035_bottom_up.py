from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        subseqLengthAt = [[0] * (len(nums2) + 1) for _ in range(len(nums1)+1)]
        for i1 in range(1, len(nums1)+1):
            for i2 in range(1, len(nums2)+1):
                if nums1[i1-1] == nums2[i2-1]:
                    subseqLengthAt[i1][i2] = 1 + subseqLengthAt[i1-1][i2-1]
                else:
                    subseqLengthAt[i1][i2] = max(subseqLengthAt[i1-1][i2], subseqLengthAt[i1][i2-1])
        return subseqLengthAt[-1][-1]








