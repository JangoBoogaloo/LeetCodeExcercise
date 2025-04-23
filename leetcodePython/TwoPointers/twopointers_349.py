from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        intersection = set()
        num1Index, num2Index = 0, 0
        while num1Index < len(nums1) and num2Index < len(nums2):
            if nums1[num1Index] < nums2[num2Index]:
                num1Index += 1
            elif nums1[num1Index] > nums2[num2Index]:
                num2Index += 1
            else:
                intersection.add(nums2[num2Index])
                num1Index += 1
                num2Index += 1
        return list(intersection)


class SolutionSet:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

