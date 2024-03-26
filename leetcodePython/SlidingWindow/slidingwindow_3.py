class SolutionBruteforce:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_length = 0
        for start in range(0, n):
            chars = set()
            for end in range(start, n):
                if s[end] in chars:
                    break
                max_length = max(max_length, end - start + 1)
                chars.add(s[end])
        return max_length


class SolutionSlidingWindow:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        chars = set()
        max_length = 0
        while right < len(s):
            new_char = s[right]
            while new_char in chars:
                old_char = s[left]
                chars.remove(old_char)
                left += 1
            chars.add(new_char)
            max_length = max(max_length, right-left+1)
            right += 1
        return max_length


class SolutionSlidingWindowRepeatIndexJump:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        char_index = {}
        max_length = 0
        while right < len(s):
            new_char = s[right]
            if new_char in char_index:
                left = max(char_index[new_char]+1, left)
            max_length = max(max_length, right-left+1)
            char_index[new_char] = right
            right += 1
        return max_length