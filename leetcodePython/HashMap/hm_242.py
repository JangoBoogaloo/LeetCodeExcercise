from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFreq = Counter(s)
        tFreq = Counter(t)
        for s in sFreq:
            if sFreq[s] != tFreq[s]:
                return False
            del tFreq[s]
        return len(tFreq) == 0






