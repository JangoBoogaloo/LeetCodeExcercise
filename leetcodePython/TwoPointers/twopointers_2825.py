class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i1, i2 = 0, 0
        while i1 < len(str1) and i2 < len(str2):
            if str1[i1] == str2[i2]:
                i1 += 1
                i2 += 1
                continue
            ch_num = ord(str1[i1]) - ord("a")
            new_ch = chr((ch_num + 1) % 26 + ord("a"))
            if new_ch == str2[i2]:
                i1 += 1
                i2 += 1
                continue
            i1 += 1
        if i2 == len(str2):
            return True

        return False
