import collections
from typing import List


class UF:
    def __init__(self, size: int) -> None:
        self.ranks = [0] * size
        self.parents = list(range(size))

    def find(self, a: int) -> int:
        if self.parents[a] != a:
            self.parents[a] = self.find(self.parents[a])
        return self.parents[a]

    def union(self, a: int, b: int) -> None:
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return
        if self.ranks[root_a] > self.ranks[root_b]:
            self.parents[root_b] = root_a
        elif self.ranks[root_b] > self.ranks[root_a]:
            self.parents[root_a] = root_b
        else:
            self.parents[root_b] = root_a
            self.ranks[root_a] += 1


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # [a, b]
        # s[a] < s[b] but a > b, swap
        # "cba" "bca" "bac" "abc"
        # [0, 1] [1, 2]
        # "dcba"  "cdab"
        # [0, 1] [2, 3]
        index_char_map = {}
        uf = UF(len(s))
        for a, b in pairs:
            uf.union(a, b)
            index_char_map[a] = s[a]
            index_char_map[b] = s[b]
        components = collections.defaultdict(list)
        for i in range(len(s)):
            components[uf.find(i)].append(s[i])
        for comp_chars in components.values():
            comp_chars.sort(reverse=True)
        ans = []
        for i in range(len(s)):
            ans.append(components[uf.find(i)].pop())
        return "".join(ans)
