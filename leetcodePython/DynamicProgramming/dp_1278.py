from functools import lru_cache


class Solution:
    @lru_cache(None)
    def palindromePartition(self, txt: str, k: int) -> int:
        if len(txt) == k:
            return 0
        if k == 1:
            return sum(txt[i] != txt[~i] for i in range(len(txt)//2))
        minOps = float("inf")
        for partitionIndex in range(len(txt) - k + 1):
            ops = self.palindromePartition(txt[:partitionIndex+1], 1) + self.palindromePartition(txt[partitionIndex+1:], k-1)
            minOps = min(ops,minOps)
        return minOps
