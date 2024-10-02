from itertools import accumulate
from typing import List


class Solution:
    _MOD = 10 ** 9 + 7

    def totalStrength(self, strength: List[int]) -> int:
        size = len(strength)

        index_next_small_right = [size] * size
        stack = []
        for i in range(size):
            while stack and strength[i] < strength[stack[-1]]:
                prev_i = stack.pop()
                index_next_small_right[prev_i] = i
            stack.append(i)

        index_next_small_left = [-1] * size
        stack = []
        for i in range(size - 1, -1, -1):
            while stack and strength[i] <= strength[stack[-1]]:
                prev_i = stack.pop()
                index_next_small_left[prev_i] = i
            stack.append(i)

        sum_of_sum = list(accumulate(accumulate(strength), initial=0))
        total = 0
        for i in range(size):
            l, r = index_next_small_left[i], index_next_small_right[i]
            left_sum_of_sum = sum_of_sum[i] - sum_of_sum[max(l, 0)]
            right_sum_of_sum = sum_of_sum[r] - sum_of_sum[i]
            l_count = i - l
            r_count = r - i
            total += strength[i] * (right_sum_of_sum * l_count - left_sum_of_sum * r_count) % self._MOD
        return total % self._MOD
