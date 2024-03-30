from collections import Counter

class SolutionBruteForceSlidingWindow:
    def __makeValidLengthString(self, s: str, length: int, k: int) -> bool:
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
    def __makeValidLengthString(self, s: str, length: int, k: int) -> bool:
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
        left, right, max_freq = 0, 0, 0
        freq_map = Counter()
        max_window_size = 0
        while right < len(s):
            ch = s[right]
            freq_map[ch] += 1
            max_freq = max(max_freq, freq_map[ch])
            right += 1
            window_size = right - left
            replace_move = window_size - max_freq
            if replace_move > k:
                freq_map[s[left]] -= 1
                left += 1
            max_window_size = right - left
        return max_window_size