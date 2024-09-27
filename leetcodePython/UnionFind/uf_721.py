import collections
from typing import List


class UnionFind:
    def __init__(self, size: int):
        self.parents = list(range(size))

    def find(self, a: int) -> int:
        if a != self.parents[a]:
            self.parents[a] = self.find(self.parents[a])
        return self.parents[a]

    def union(self, child: int, parent: int) -> None:
        self.parents[self.find(child)] = self.find(parent)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        ownership = {}
        for i, (name, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(i, ownership[email])
                ownership[email] = i

        owner_email_map = collections.defaultdict(list)
        for email, owner in ownership.items():
            owner_email_map[uf.find(owner)].append(email)

        ans = []
        for i, emails in owner_email_map.items():
            account = [accounts[i][0]] + sorted(emails)
            ans.append(account)
        return ans
