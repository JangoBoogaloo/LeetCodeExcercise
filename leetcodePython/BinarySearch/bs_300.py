from typing import List


class SolutionDP:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # the length of the longest increasing subsequence that ends with the i th element
        dp_sequence_length = [1] * len(nums)

        # kind of slide window or two pointer
        for right in range(1, len(nums)):
            for left in range(right):
                if nums[right] > nums[left]:
                    left_sequence_with_right = dp_sequence_length[left] + 1
                    dp_sequence_length[right] = max(dp_sequence_length[right], left_sequence_with_right)
        return max(dp_sequence_length)