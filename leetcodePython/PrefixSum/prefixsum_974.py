from typing import List
from collections import Counter


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        arr_counts = Counter()
        running_sum = 0
        res = 0
        for num in nums:
            running_sum += num
            remain = running_sum % k
            if remain == 0:
                res += 1
            res += arr_counts[remain]
            arr_counts[remain] += 1
        return res
