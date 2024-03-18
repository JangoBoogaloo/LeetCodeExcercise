class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        totalLen = len1 + len2
        i1 = i2 = 0
        result = ""
        for i in range(0, totalLen):
            if i2 >= len2:
                result += word1[i1]
                i1 += 1
            elif i1 >= len1:
                result += word2[i2]
                i2 += 1
            elif i % 2 == 0:
                result += word1[i1]
                i1 += 1
            else:
                result += word2[i2]
                i2 += 1
        return result

if __name__ == '__main__':
    solution = Solution()
    result = solution.mergeAlternately("ace", "bdf")
    print(result)