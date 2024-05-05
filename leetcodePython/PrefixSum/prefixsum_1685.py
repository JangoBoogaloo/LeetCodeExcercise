from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix_sum = []
        run_sum = 0
        for num in nums:
            run_sum += num
            prefix_sum.append(run_sum)
        n = len(nums)
        ans = []
        for i in range(len(nums)):
            left_sum = prefix_sum[i] - nums[i]
            left_count = i
            left_total = left_count * nums[i] - left_sum

            right_sum = prefix_sum[-1] - prefix_sum[i]
            right_count = n - i - 1
            right_total = right_sum - right_count * nums[i]
            ans.append(left_total + right_total)
        return ans


class SolutionInplace:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        left_sum = 0
        n = len(nums)
        ans = []
        for i in range(len(nums)):
            left_count = i
            left_total = left_count * nums[i] - left_sum

            right_count = n - 1 - i
            right_sum = total_sum - left_sum - nums[i]
            right_total = right_sum - right_count * nums[i]
            ans.append(left_total + right_total)
            left_sum += nums[i]
        return ans
