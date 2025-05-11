from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n-1:
            return -1
        trustCount = [0] * (n+1)
        trustedCount = [0] * (n+1)
        for truster, trustee in trust:
            trustCount[truster] += 1
            trustedCount[trustee] += 1
        for people in range(1, n+1):
            if trustCount[people] == 0 and trustedCount[people] == n - 1:
                return people
        return -1






