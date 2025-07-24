class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        tIndexOf = {}
        for i in range(len(t)):
            tIndexOf[t[i]] = i

        answer = 0
        for sIndex in range(len(s)):
            answer += abs(sIndex - tIndexOf[s[sIndex]])
        return answer