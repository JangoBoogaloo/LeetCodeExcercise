from typing import List


class Solution:
    def _findMedian(self, smallerArray: List[int], biggerArray: List[int]) -> float:
        size_1, size_2 = len(smallerArray), len(biggerArray)
        left, right = 0, len(smallerArray)

        while left <= right:
            # [...smallMid...][..totalMid.........]

            # [--------------totalHalf--------------][--------------totalHalf--------------]
            # [smallHalf][smallHalf][--------bigHalf-----------][---------bigHalf----------]
            smallMid = (left + right) // 2
            totalMid = (len(smallerArray) + len(biggerArray) + 1) // 2
            mid_bigger = totalMid - smallMid

            if smallMid == 0:
                maxLeftA = float("-inf")
            else:
                maxLeftA = smallerArray[smallMid - 1]

            if smallMid == len(smallerArray):
                minRightA = float("inf")
            else:
                minRightA = smallerArray[smallMid]

            if mid_bigger == 0:
                maxLeftB = float("-inf")
            else:
                maxLeftB = biggerArray[mid_bigger - 1]
            if mid_bigger == len(biggerArray):
                minRightB = float("inf")
            else:
                minRightB = biggerArray[mid_bigger]
            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (size_1 + size_2) % 2 == 0:
                    maxLeft = max(maxLeftA, maxLeftB)
                    minRight = min(minRightA, minRightB)
                    return (maxLeft + minRight) / 2
                else:
                    return max(maxLeftA, maxLeftB)
            elif maxLeftA > minRightB:
                right = smallMid - 1
            else:
                left = smallMid + 1

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self._findMedian(nums2, nums1)
        return self._findMedian(nums1, nums2)
