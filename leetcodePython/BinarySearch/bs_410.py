from typing import List


class Solution:
    @staticmethod
    def _sub_count_with_sum(nums: List[int], max_sum: int) -> int:
        curr_sum = 0
        count = 1
        for num in nums:
            if curr_sum + num > max_sum:
                count += 1
                curr_sum = 0
            curr_sum += num
        return count

    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        while left < right:
            guess_sum = (left + right) // 2
            if self._sub_count_with_sum(nums, guess_sum) > k:
                left = guess_sum + 1
            else:
                right = guess_sum
        return left

if __name__ == "__main__":
    sol = Solution()
    ans = sol.splitArray([1,2,3,4,5], 2)
    print(ans)
