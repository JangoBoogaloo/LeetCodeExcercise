from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # remain 0 have no valid have 0 remain.
        remain_index = {0: -1}
        run_sum = 0
        for i, num in enumerate(nums):
            run_sum += num
            remain = run_sum % k
            if remain not in remain_index:
                # Set the earliest index that have the remain, to build the maximum sub array.
                # So size can possibly be >2
                remain_index[remain] = i
            else:
                if i - remain_index[remain] >= 2:
                    return True
        return False
