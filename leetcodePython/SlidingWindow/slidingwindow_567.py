from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left, right, valid = 0, 0, 0
        need = Counter(s1)
        window = Counter()
        while right < len(s2):
            new_ch = s2[right]
            right += 1
            if new_ch in need:
                window[new_ch] += 1
                if window[new_ch] == need[new_ch]:
                    valid += 1
            # Shrink this fucking window until window size is same as s1
            while right - left >= len(s1):
                if valid == len(need):
                    return True
                old_ch = s2[left]
                left += 1
                if old_ch in need:
                    if window[old_ch] == need[old_ch]:
                        valid -= 1
                    window[old_ch] -= 1
        return False



if __name__ == "__main__":
    solution = Solution()
    w = solution.checkInclusion("ab", "eidboaoo")
    print(w)