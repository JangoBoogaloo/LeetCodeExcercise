from collections import Counter


class SolutionBruteForceSlidingWindow:
    @staticmethod
    def __makeValidLengthString(s: str, length: int, k: int) -> bool:
        left, right, max_freq = 0, 0, 0
        freq_map = Counter()
        while right < len(s):
            ch = s[right]
            freq_map[ch] += 1
            right += 1
            if right-left > length:
                freq_map[s[left]] -= 1
                left += 1
            max_freq = max(max_freq, freq_map[ch])
            if length - max_freq <= k:
                return True
        return False

    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        for i in range(1,len(s)+1):
            if self.__makeValidLengthString(s, i, k):
                result = i
            else:
                break
        return result


class SolutionSlidingWindowBinarySearch:
    @staticmethod
    def __makeValidLengthString(s: str, length: int, k: int) -> bool:
        left, right, max_freq = 0, 0, 0
        freq_map = Counter()
        while right < len(s):
            ch = s[right]
            freq_map[ch] += 1
            right += 1
            if right-left > length:
                freq_map[s[left]] -= 1
                left += 1
            max_freq = max(max_freq, freq_map[ch])
            if length - max_freq <= k:
                return True
        return False

    def characterReplacement(self, s: str, k: int) -> int:
        left = 1
        right = len(s)+1
        while right - left > 1:
            mid = left + (right - left) // 2
            if self.__makeValidLengthString(s, mid, k):
                left = mid
            else:
                right = mid
        return left


class SolutionSlidingWindow:
    def characterReplacement(self, s: str, k: int) -> int:
        left, max_freq = 0, 0
        freq_map = Counter()
        right: int = 0
        for right in range(len(s)):
            freq_map[s[right]] += 1
            max_freq = max(max_freq, freq_map[s[right]])
            window_size = right - left + 1
            operations = window_size - max_freq
            if operations > k:
                freq_map[s[left]] -= 1
                left += 1
        return right - left + 1
