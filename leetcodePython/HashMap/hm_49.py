from collections import Counter, defaultdict
from typing import List


class Solution:
    def _hash(self, txt: str) -> str:
        txtFreq = Counter(txt)
        txtKeys = sorted(txtFreq.keys())
        result = []
        for key in txtKeys:
            result.append(f"{key}{txtFreq[key]}")
        return "".join(result)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)
        for txt in strs:
            key = self._hash(txt)
            answer[key].append(txt)
        return list(answer.values())





