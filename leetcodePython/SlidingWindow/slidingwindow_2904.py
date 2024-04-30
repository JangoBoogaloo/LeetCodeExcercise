class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ''
        left = 0
        for right, ch in enumerate(s):
            if ch == '1': k -= 1
            while k < 0 or left < right and s[left] == '0':
                if s[left] == '1':
                    k += 1
                left += 1
            if k == 0 and (ans == '' or len(ans) > right-left+1 or len(ans) == right-left+1 and ans > s[left : right+1]):
                ans = s[left : right+1]
        return ans