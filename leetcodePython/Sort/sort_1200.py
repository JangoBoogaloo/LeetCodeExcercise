from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff = []
        for i in range(len(arr) - 1):
            diff.append(abs(arr[i + 1] - arr[i]))
        min_diff = min(diff)
        ans = []
        for i in range(len(arr) - 1):
            if (arr[i + 1] - arr[i]) == min_diff:
                ans.append([arr[i], arr[i + 1]])
        return ans
