class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        prev_ch = 'z'
        vowel_count = 0
        left = 0
        longest = 0
        for right in range(len(word)):
            if word[right] > prev_ch:
                vowel_count += 1
            elif word[right] < prev_ch:
                vowel_count = 1
                left = right
            if vowel_count == len(vowels):
                longest = max(longest, right - left + 1)
            prev_ch = word[right]

        return longest
