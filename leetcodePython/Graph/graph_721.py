from typing import List
from union_find import UF
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accountOfEmail = {}
        uf = UF()
        for accountId in range(len(accounts)):
            uf.add(accountId)
            for email in accounts[accountId][1:]:
                if email in accountOfEmail:
                    uf.union(accountId, accountOfEmail[email])
                accountOfEmail[email] = accountId

        emailsOfAccount = defaultdict(list)
        for email, accountId in accountOfEmail.items():
            emailsOfAccount[uf.find(accountId)].append(email)

        answer = []
        for accountId, emails in emailsOfAccount.items():
            answer.append([accounts[accountId][0]] + sorted(emails))
        return answer






