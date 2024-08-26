from typing import List


class SolutionMergeSort:
    @staticmethod
    def _mergeCompare(nums1: List[int], nums2: List[int], index1: int, index2: int) -> tuple[int, int, int]:
        if index1 == len(nums1):
            ans = nums2[index2]
            index2 += 1
            return ans, index1, index2

        if index2 == len(nums2):
            ans = nums1[index1]
            index1 += 1
            return ans, index1, index2

        if nums1[index1] < nums2[index2]:
            ans = nums1[index1]
            index1 += 1
        else:
            ans = nums2[index2]
            index2 += 1
        return ans, index1, index2

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        index1, index2 = 0, 0

        before_middle = (len(nums1) + len(nums2)) // 2

        if (len(nums1) + len(nums2)) % 2 == 0:
            before_middle -= 1

        for _ in range(before_middle):
            _, index1, index2 = self._mergeCompare(nums1, nums2, index1, index2)

        if (len(nums1) + len(nums2)) % 2 == 0:
            smaller, index1, index2, = self._mergeCompare(nums1, nums2, index1, index2)
            bigger, index1, index2 = self._mergeCompare(nums1, nums2, index1, index2)
            return (smaller + bigger) / 2
        else:
            median, _, _ = self._mergeCompare(nums1, nums2, index1, index2)
            return median
