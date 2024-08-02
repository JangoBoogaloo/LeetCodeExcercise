import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = collections.defaultdict(list)
        for str in strs:
            anagram[''.join(sorted(str))].append(str)

        ans = []
        for key in anagram:
            ans.append(anagram[key])
        return ans

if __name__ == '__main__':
    sol = Solution()
    a = sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(a)