from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left, right, valid = 0, 0, 0
        need = Counter(p)
        window = Counter()
        result = []
        while right < len(s):
            new_ch = s[right]
            right += 1 # we are adding a character in our sliding window
            if new_ch in need:
                window[new_ch] += 1
                if window[new_ch] == need[new_ch]:
                    valid += 1
            while right - left >= len(p):
                if valid == len(need):
                    result.append(left)
                old_ch = s[left]
                left += 1
                if old_ch in need:
                    if window[old_ch] == need[old_ch]:
                        valid -= 1
                    window[old_ch] -= 1
        return result

if __name__ == "__main__":
    solution = Solution()
    result = solution.findAnagrams("abab", "ab")
    print(result) # expect to get [0, 6]

