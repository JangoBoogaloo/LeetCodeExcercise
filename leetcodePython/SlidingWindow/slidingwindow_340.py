from collections import Counter
class SolutionBasicSlidingWindow:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        char_freq = Counter()
        left, right, length = 0, 0, 0
        while right < len(s):
            ch = s[right]
            char_freq[ch] += 1
            right += 1
            while len(char_freq) > k:
                old_ch = s[left]
                char_freq[old_ch] -= 1
                if char_freq[old_ch] == 0:
                    char_freq.pop(old_ch)
                left += 1
            length = max(length, right-left)
        return length

class SolutionMaxWindowSlidingWindow:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        max_size = 0
        counter = Counter()

        for right in range(len(s)):
            counter[s[right]] += 1

            # we don't care the current window valid, we only need to find a max window
            if len(counter) > k:
                # when distinct is more than k, we shift max window but not increase window
                counter[s[right - max_size]] -= 1
                if counter[s[right - max_size]] == 0:
                    del counter[s[right - max_size]]
            else:
                max_size += 1

        return max_size