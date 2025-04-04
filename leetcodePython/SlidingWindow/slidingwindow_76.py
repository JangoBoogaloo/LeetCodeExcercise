from collections import Counter

class SolutionSlidingWindow:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        left, right, match = 0, 0, 0
        min_size = float('inf')
        min_left = 0
        min_right = 0
        need = Counter(t)
        window = Counter()
        while right < len(s):
            ch = s[right]
            window[ch] += 1
            if ch in need and window[ch] == need[ch]:
                match += 1
            while left <= right and match == len(need):
                if min_size > right - left + 1:
                    min_size = right - left + 1
                    min_left = left
                    min_right = right
                old_ch = s[left]
                left += 1
                window[old_ch] -= 1
                if old_ch in need and window[old_ch] < need[old_ch]:
                    match -= 1
            right += 1
        if min_size == float('inf'):
            return ""
        else:
            return s[min_left:min_right+1]


if __name__ == "__main__":
    solution = SolutionSlidingWindow()
    w = solution.minWindow("ADOBECODEBANC", "ABC")
    print(w)