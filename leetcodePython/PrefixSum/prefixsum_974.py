from typing import List
from collections import Counter

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        arr_counts = Counter()
        running_sum = 0
        res = 0
        for num in nums:
            running_sum += num
            # S(n) % k = r
            remain = running_sum % k
            if remain == 0:
                res += 1
            # S(i) ...... S(j) each of them % k = r
            # So we potentially have that many combination
            res += arr_counts[remain]
            arr_counts[remain] += 1
        return res