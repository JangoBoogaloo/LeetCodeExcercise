from typing import List


class SolutionDP:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp_sequence_length = [1] * len(nums)

        # kind of slide window or two pointer
        for right in range(1, len(nums)):
            for left in range(right):
                if nums[right] > nums[left]:
                    dp_sequence_length[right] = max(dp_sequence_length[right], dp_sequence_length[left] + 1)
        return max(dp_sequence_length)