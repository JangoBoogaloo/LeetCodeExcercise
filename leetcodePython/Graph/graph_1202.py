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








import pytest
target = Solution()

@pytest.mark.parametrize("text, pairs, expect",
[
    ("cab", [[0, 2]], "bac"),
    ("dcab", [[0, 3], [1, 2]], "bacd"),
    ("dcab", [[0, 3], [1, 2], [0, 2]], "abcd"),
])
def test_smallestStringWithSwaps(text, pairs, expect):
    assert target.smallestStringWithSwaps(text, pairs) == expect