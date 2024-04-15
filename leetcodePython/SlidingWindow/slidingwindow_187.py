from typing import List
from collections import Counter

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        ans = set()
        for end in range(10, len(s)+1):
            substr = s[end-10:end]
            if substr in seen:
                ans.add(substr)
            seen.add(substr)
        return ans