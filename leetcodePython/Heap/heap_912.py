from typing import List


class Solution:
    def _heapify(self, nums: List[int], root_index: int, end_index: int):
        left_child_index = 2 * root_index + 1
        right_child_index = 2 * root_index + 2

        largest_index = root_index
        if left_child_index < end_index and nums[largest_index] < nums[left_child_index]:
            largest_index = left_child_index
        if right_child_index < end_index and nums[largest_index] < nums[right_child_index]:
            largest_index = right_child_index

        if largest_index != root_index:
            nums[largest_index], nums[root_index] = nums[root_index], nums[largest_index]
            self._heapify(nums, largest_index, end_index)

    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(length // 2 + 1)[::-1]:
            self._heapify(nums, i, length)

        for i in range(length)[::-1]:
            nums[i], nums[0] = nums[0], nums[i]
            self._heapify(nums, 0, i)
        return nums


if __name__ == "__main__":
    sol = Solution()
    sol.sortArray([5,4,3,2,7])