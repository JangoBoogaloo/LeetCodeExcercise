class SolutionSlidingWindow:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        char_set = set()
        max_length = 0
        for right in range(len(s)):
            new_char = s[right]
            while new_char in char_set:
                old_char = s[left]
                char_set.remove(old_char)
                left += 1
            char_set.add(new_char)
            max_length = max(max_length, right - left + 1)
        return max_length


class SolutionSlidingWindowRepeatIndexJump:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        existing_char_map = {}
        max_length = 0
        for right in range(len(s)):
            new_char = s[right]
            if new_char in existing_char_map:
                prev_char_index = existing_char_map[new_char]
                left = max(prev_char_index+1, left)
            existing_char_map[new_char] = right
            max_length = max(max_length, right - left + 1)
        return max_length
