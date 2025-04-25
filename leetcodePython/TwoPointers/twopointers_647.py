class Solution:
    def _countAroundCenter(self, s: str, left_center: int, right_center: int) -> int:
        total = 0
        while left_center >=0 and right_center < len(s):
            if s[left_center] != s[right_center]:
                break
            left_center -= 1
            right_center += 1
            total += 1
        return total

    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            ans += self._countAroundCenter(s, i, i)
            ans += self._countAroundCenter(s, i, i+1)
        return ans