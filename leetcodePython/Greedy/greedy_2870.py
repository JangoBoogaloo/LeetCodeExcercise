import collections
import math
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        num_freq = collections.Counter(nums)
        operations = 0
        for num in num_freq.values():
            if num == 1:
                return -1
            operations += math.ceil(num / 3)
        return operations


if __name__ == "__main__":
    sol = Solution()
    print(sol.minOperations([14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]))