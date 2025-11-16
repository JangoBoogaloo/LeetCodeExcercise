class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i1 = i2 = 0
        while i1 < len(str1) and i2 < len(str2):
            ch1, ch2 = str1[i1], str2[i2]
            if ch1 == 'z' and ch2 == 'a':
                i2 += 1
            elif ch1 == ch2:
                i2 += 1
            elif ord(ch2) - ord(ch1) == 1:
                i2 += 1
            i1 += 1
        return i2 == len(str2)








