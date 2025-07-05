from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        trusters, trustees = set(), set()
        trusted = defaultdict(set)
        for truster, trustee in trust:
            trusters.add(truster)
            trustees.add(trustee)
            trusted[trustee].add(truster)
        judgeSet = (trustees - trusters)
        if len(judgeSet) != 1:
            return -1
        potentialJudge = judgeSet.pop()
        if len(trusted[potentialJudge]) == (n - 1):
            return potentialJudge
        return -1