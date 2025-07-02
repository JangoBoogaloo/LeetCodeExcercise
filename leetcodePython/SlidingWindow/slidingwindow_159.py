from collections import Counter


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: 'str') -> 'int':
        # sol = slidingwindow_340.SolutionMaxWindowSlidingWindow()
        # return sol.lengthOfLongestSubstringKDistinct(s, 2)

        window_freq = Counter()
        left = 0
        for right in range(len(s)):
            new_ch = s[right]
            window_freq[new_ch] += 1
            if len(window_freq) > 2:
                old_ch = s[left]
                window_freq[old_ch] -= 1
                if window_freq[old_ch] == 0:
                    window_freq.pop(old_ch)
                left += 1
        return right - left + 1
