from collections import Counter


class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        left = 0
        res = len(s)
        require = len(s)//4
        for right, ch in enumerate(s):
            count[ch] -= 1
            while left < len(s) and all(count[i] <= require for i in 'QWER'):
                # when the sub string size is 0, string is already balanced
                if left > right:
                    return 0
                res = min(res, right-left+1)
                count[s[left]] += 1
                left += 1
        return res