from typing import List


class SolutionBruteForce:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if len(arr) == 0:
            return k
        missing_btw_1 = arr[0] - 1
        # if the kth missing is less than arr[0]
        if k <= missing_btw_1:
            return k

        k -= missing_btw_1

        for i in range(len(arr) - 1):
            curr_missing = arr[i + 1] - arr[i] - 1
            if k <= curr_missing:
                return arr[i] + k
            k -= curr_missing

        return arr[-1] + k


class SolutionBS:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid_index = (left + right) // 2
            expect_num = mid_index + 1
            if arr[mid_index] - expect_num < k:
                left = mid_index + 1
            else:
                right = mid_index - 1

        # At the end of the loop, left = right + 1,
        # and the kth missing is in-between arr[right] and arr[left].
        # The number of integers missing before arr[right] is
        # arr[right] - right - 1 -->
        # the number to return is
        # arr[right] + k - (arr[right] - right - 1) = k + left
        return left + k
