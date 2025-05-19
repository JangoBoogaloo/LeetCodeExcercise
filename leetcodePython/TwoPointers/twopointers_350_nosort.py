from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        counter1 = Counter(nums1)
        intersect = []
        for num in nums2:
            if counter1[num] > 0:
                counter1[num] -= 1
                intersect.append(num)
        return intersect




