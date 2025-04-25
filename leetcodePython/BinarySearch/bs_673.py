from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # the length of the longest increasing subsequence that ends with the i th element
        dp_sequence_length = [1] * len(nums)
        # the count of the longest increasing subsequences that ends with the i th element
        dp_count_lis = [1] * len(nums)

        # kind of slide window or two pointer
        for right in range(1, len(nums)):
            for left in range(right):
                if nums[left] < nums[right]:
                    left_sequence_with_right = dp_sequence_length[left] + 1
                    if left_sequence_with_right > dp_sequence_length[right]:
                        dp_sequence_length[right] = left_sequence_with_right
                        # use [left] sequence with num[right] to build another sequence, so we get [left] counts
                        dp_count_lis[right] = dp_count_lis[left]
                    elif left_sequence_with_right == dp_sequence_length[right]:
                        # can be [left] sequence with num[right] or [right] sequence, so we have to add all counts
                        dp_count_lis[right] = dp_count_lis[right] + dp_count_lis[left]
        max_length = max(dp_sequence_length)
        total = 0
        for i in range(len(nums)):
            if dp_sequence_length[i] == max_length:
                total += dp_count_lis[i]
        return total
