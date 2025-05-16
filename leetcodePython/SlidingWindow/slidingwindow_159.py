from collections import Counter


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: 'str') -> 'int':
        max_size = 0
        counter = Counter()

        for right in range(len(s)):
            counter[s[right]] += 1

            # we don't care the current window valid, we only need to find a max window
            if len(counter) > 2:
                # when distinct is more than k, we shift max window but not increase window
                counter[s[right - max_size]] -= 1
                if counter[s[right - max_size]] == 0:
                    del counter[s[right - max_size]]
            else:
                max_size += 1

        return max_size