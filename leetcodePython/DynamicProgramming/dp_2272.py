import collections
from math import inf


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

            if major_count < minor_count and minor_remain > 0:
                major_count = 0
                minor_count = 0
                continue

            if minor_count > 0:
                curr_variance = major_count - minor_count
                max_variance = max(max_variance, curr_variance)

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


class SolutionDP:
    def largestVariance(self, s: str) -> int:
        BASE_a = ord("a")
        count = [0] * 26
        chars = [ord(major) - BASE_a for major in set(s)]
        min_diff = [[inf] * 26 for _ in range(26)]
        prev_diff = [[0] * 26 for _ in range(26)]
        res = 0

        for major in s:
            major = ord(major) - BASE_a
            count[major] += 1
            if count[major] == 1:
                res = max(count) - 1
            for minor in chars:
                if major == minor:
                    continue
                if prev_diff[minor][major] < min_diff[minor][major]:
                    min_diff[minor][major] = prev_diff[minor][major]

                cur_diff = count[major] - count[minor]
                if res < cur_diff - min_diff[major][minor]:
                    res = cur_diff - min_diff[major][minor]

                prev_diff[minor][major] = -cur_diff

        return res
