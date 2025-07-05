from typing import List
from union_find import UF
from collections import defaultdict

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UF()
        [uf.add(i) for i in range(len(s))]

        for i1, i2 in pairs:
            uf.union(i1,i2)
        charsForComponent = defaultdict(list)

        for i in range(len(s)):
            charsForComponent[uf.find(i)].append(s[i])

        for chars in charsForComponent.values():
            chars.sort(reverse=True)
        ans = []
        for i in range(len(s)):
            lastCharForComponent = charsForComponent[uf.find(i)].pop()
            ans.append(lastCharForComponent)
        return "".join(ans)







