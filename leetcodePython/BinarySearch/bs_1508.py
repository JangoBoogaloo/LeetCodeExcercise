import heapq
from typing import List


class SolutionBruteForce:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        for start in range(len(nums)):
            curr_sum = 0
            for end in range(start, len(nums)):
                curr_sum += nums[end]
                sums.append(curr_sum)
        sums.sort()
        return sum(sums[left - 1:right]) % (10 ** 9 + 7)


class SolutionSlidingWindowBS:
    @staticmethod
    def _count_and_sum_target(nums: List[int], n: int, target: int) -> tuple[int, int]:
        curr_sum = 0
        left = 0
        window_sum = 0
        count = 0
        total_sum = 0
        for right in range(n):
            curr_sum += nums[right]
            #
            window_sum += nums[right] * (right - left + 1)
            while curr_sum > target:
                window_sum -= curr_sum
                curr_sum -= nums[left]
                left += 1
            count += right - left + 1
            total_sum += window_sum
        return count, total_sum

    def _sum_first_k(self, nums: List[int], min_sum: int, max_sum: int, n: int, k: int) -> int:
        left, right = min_sum, max_sum

        while left <= right:
            mid = (left + right) // 2
            count, _ = self._count_and_sum_target(nums, n, mid)
            if count >= k:
                right = mid - 1
            else:
                left = mid + 1

        count, total_sum = self._count_and_sum_target(nums, n, left)
        return total_sum - left * (count - k)

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        min_sum = min(nums)
        max_sum = sum(nums)
        sum_to_right = self._sum_first_k(nums, min_sum, max_sum, n, right)
        sum_to_left = self._sum_first_k(nums, min_sum, max_sum, n, left - 1)
        result = sum_to_right - sum_to_left
        mod = 10 ** 9 + 7
        return (result + mod) % mod
