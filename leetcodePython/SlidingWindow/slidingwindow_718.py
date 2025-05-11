from typing import List


class Solution:
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


class SolutionBinarySearch:
    # Binary Search Approach
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        N, M = len(nums1), len(nums2)

        def ok(k):
            # the idea is to use binary search to find the length `k`
            # then we check if there is any nums1[i : i + k] == nums2[i : i + k]
            s = set(tuple(nums1[i: i + k]) for i in range(len(nums1) - k + 1))
            return any(tuple(nums2[i: i + k]) in s for i in range(M - k + 1))

        # init possible boundary
        l, r = 0, min(N, M)
        while l < r:
            # get the middle one
            # for even number of elements, take the upper one
            m = (l + r + 1) // 2
            if ok(m):
                # include m
                l = m
            else:
                # exclude m
                r = m - 1
        return l

if __name__ == "__main__":
    sol = SolutionBinarySearch()
    ans = sol.findLength([1,2,3,2,1], [3,2,1,4,7])