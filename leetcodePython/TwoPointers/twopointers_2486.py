class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_i = int(0)
        for ch in s:
            if t_i >= len(t):
                return 0
            if ch == t[t_i]:
                t_i += 1
        return len(t) - t_i
