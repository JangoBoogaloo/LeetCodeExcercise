class Solution:
    def countPalindromicSubsequence(self, txt: str) -> int:
        charSet = set(txt)
        count = 0
        for ch in charSet:
            chLeft, chRight = txt.find(ch), txt.rfind(ch)
            chMidSet = set(txt[chLeft+1:chRight])
            count += len(chMidSet)
        return count