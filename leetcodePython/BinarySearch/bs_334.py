from bisect import bisect_left
from typing import List


class SolutionSubSequenceBinarySearch:
    def increasingTriplet(self, nums: List[int]) -> bool:
        sub_seq = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > sub_seq[-1]:
                sub_seq.append(nums[i])
                if len(sub_seq) == 3:
                    return True
            else:
                index = bisect_left(sub_seq, nums[i])
                sub_seq[index] = nums[i]
        return False


class SolutionSubSequenceSpecial:
    def increasingTriplet(self, nums: List[int]) -> bool:
        sequence = [float('inf')] * 3
        for num in nums:
            if num <= sequence[0]:
                sequence[0] = num
            elif num <= sequence[1]:
                sequence[1] = num
            else:
                return True
        return False
