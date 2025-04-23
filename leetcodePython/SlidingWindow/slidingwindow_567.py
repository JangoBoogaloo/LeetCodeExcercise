from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_freq = Counter(s1)
        window_freq = Counter()
        left = 0
        matched = 0
        for right in range(len(s2)):
            right_ch = s2[right]
            if right_ch in s1_freq:
                window_freq[right_ch] += 1
                if window_freq[right_ch] == s1_freq[right_ch]:
                    matched += 1
            while right - left + 1 >= len(s1):
                if matched == len(s1_freq):
                    return True
                left_ch = s2[left]
                left += 1
                if left_ch in s1_freq:
                    if window_freq[left_ch] == s1_freq[left_ch]:
                        matched -= 1
                    window_freq[left_ch] -= 1
        return False


if __name__ == "__main__":
    solution = Solution()
    w = solution.checkInclusion("ab", "eidboaoo")
    print(w)