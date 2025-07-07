from typing import List


class SolutionSlidingWindow:
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


class Solution:
    @staticmethod
    def _subarray_len_exist(nums1: List[int], nums2: List[int], length: int) -> bool:
        num1_sub_arr_set = set(tuple(nums1[i: i+length]) for i in range(len(nums1)-length+1))
        for i in range(len(nums2)-length+1):
            if tuple(nums2[i: i+length]) in num1_sub_arr_set:
                return True
        return False

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        left, right = 0, min(len(nums1), len(nums2))
        while left < right:
            guess_length = (left + right + 1) // 2
            if self._subarray_len_exist(nums1, nums2, guess_length):
                left = guess_length
            else:
                right = guess_length - 1
        return left
