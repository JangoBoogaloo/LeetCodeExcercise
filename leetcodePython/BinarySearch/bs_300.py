import bisect
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


class SolutionBuildSequence:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub: List[int]
        sub = [nums[0]]

        for num in nums[1:]:
            # new data is smaller, insert data in to sequence, to build a possible different longer array later
            if num <= sub[-1]:
                i = 0
                while sub[i] < num:
                    i += 1
                # sub[i] >= num
                sub[i] = num
            else:
                sub.append(num)
        # not always generate a valid subsequence of the input, but the length of the subsequence is valid
        return len(sub)


class SolutionBuildSequenceBS:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub: List[int]
        sub = []
        for num in nums:
            i = bisect.bisect_left(sub, num)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)
            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num
        return len(sub)
