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


class SolutionBS:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        size_1, size_2 = len(nums1), len(nums2)
        left, right = 0, size_1

        while left <= right:
            mid_smaller = (left + right) // 2
            mid_total = (size_1 + size_2 + 1) // 2
            mid_bigger = mid_total - mid_smaller

            maxLeftA = float("-inf") if mid_smaller == 0 else nums1[mid_smaller - 1]
            minRightA = float("inf") if mid_smaller == size_1 else nums1[mid_smaller]

            maxLeftB = float("-inf") if mid_bigger == 0 else nums2[mid_bigger - 1]
            minRightB = float("inf") if mid_bigger == size_2 else nums2[mid_bigger]

            # [ maxLeftA ]    [ minRightA ]
            # [ maxLeftB ]    [ minRightB ]
            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (size_1 + size_2) % 2 == 0:
                    maxLeft = max(maxLeftA, maxLeftB)
                    minRight = min(minRightA, minRightB)
                    return (maxLeft + minRight) / 2
                else:
                    return max(maxLeftA, maxLeftB)
            elif maxLeftA > minRightB:
                right = mid_smaller - 1
            else:
                left = mid_smaller + 1