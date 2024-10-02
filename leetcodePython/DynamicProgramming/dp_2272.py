import collections


class SolutionBruteForce:

    def _max_variance_between(self, major: str, minor: str, s: str, minor_remain: int) -> int:
        major_count = minor_count = 0
        max_variance = 0
        for ch in s:
            if ch == major:
                major_count += 1
            elif ch == minor:
                minor_count += 1
                minor_remain -= 1

            if minor_count > 0:
                curr_variance = major_count - minor_count
                max_variance = max(max_variance, curr_variance)
            if major_count < minor_count and minor_remain > 0:
                major_count = 0
                minor_count = 0
        return max_variance

    def largestVariance(self, s: str) -> int:
        char_freq = collections.Counter(s)
        ans = 0
        for major in char_freq.keys():
            for minor in char_freq.keys():
                if major == minor:
                    continue
                minor_remain = char_freq[minor]
                curr_max = self._max_variance_between(major, minor, s, minor_remain)
                ans = max(ans, curr_max)
        return ans
