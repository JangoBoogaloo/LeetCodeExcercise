from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right, window_sum = 0, 0, 0
        min_len = float('inf')
        while right < len(nums):
            window_sum += nums[right]
            right += 1
            while left < right and window_sum >= target:
                min_len = min(min_len, right-left)
                window_sum -= nums[left]
                left += 1
        if min_len == float('inf'):
            return 0
        return min_len

if __name__ == "__main__":
    solution = Solution()
    print(solution.minSubArrayLen(7, [2,3,1,2,4,3]))