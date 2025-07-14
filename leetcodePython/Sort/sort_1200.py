from typing import List
from math import inf

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = inf
        answer = []
        for i in range(1, len(arr)):
            currDiff = arr[i] - arr[i-1]
            if currDiff > minDiff:
                continue
            if currDiff < minDiff:
                minDiff = currDiff
                answer = []
            answer.append([arr[i-1], arr[i]])
        return answer