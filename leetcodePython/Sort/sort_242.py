import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = collections.Counter()
        for ch in s:
            s_count[ch] += 1

        to_match = len(s_count)
        for ch in t:
            s_count[ch] -= 1
            if s_count[ch] < 0:
                return False
            if s_count[ch] == 0:
                to_match -= 1
        return to_match == 0

