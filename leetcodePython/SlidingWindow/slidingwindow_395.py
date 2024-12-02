from collections import Counter


class SolutionRecursion:
    def longestSubstring(self, s: str, k: int) -> int:
        char_count = Counter(s)
        max_length = 0
        for char in char_count:
            if char_count[char] < k:
                for str_without_char in s.split(char):
                    if len(str_without_char) >= k:
                        substr_max_length = self.longestSubstring(str_without_char, k)
                        max_length = max(max_length, substr_max_length)
                return max_length
        return len(s)
