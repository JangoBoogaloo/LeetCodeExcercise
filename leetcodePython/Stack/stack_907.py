from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        smaller_element_index = []
        dp = [0] * len(arr)
        for i, data in enumerate(arr):
            while smaller_element_index and arr[smaller_element_index[-1]] >= arr[i]:
                smaller_element_index.pop()

            if smaller_element_index:
                smaller_index = smaller_element_index[-1]
                dp[i] = dp[smaller_index] + (i-smaller_index) * arr[i]
            else:
                dp[i] = (i + 1) * arr[i]
            smaller_element_index.append(i)
        return sum(dp) % MOD