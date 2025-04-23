from typing import List


class Solution:
    def _heapifyMaxHeap(self, nums: List[int], rootIndex: int, indexLimit: int):
        leftIndex = 2 * rootIndex + 1
        rightIndex = 2 * rootIndex + 2

        largestIndex = rootIndex
        if leftIndex < indexLimit and nums[largestIndex] < nums[leftIndex]:
            largestIndex = leftIndex
        if rightIndex < indexLimit and nums[largestIndex] < nums[rightIndex]:
            largestIndex = rightIndex

        if largestIndex != rootIndex:
            nums[largestIndex], nums[rootIndex] = nums[rootIndex], nums[largestIndex]
            self._heapifyMaxHeap(nums, largestIndex, indexLimit)

    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(length // 2 + 1)[::-1]:
            self._heapifyMaxHeap(nums, i, length)

        for i in range(length)[::-1]:
            nums[i], nums[0] = nums[0], nums[i]
            self._heapifyMaxHeap(nums, 0, i)
        return nums
