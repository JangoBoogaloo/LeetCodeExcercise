import collections
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = collections.Counter(arr)
        sorted_freq = sorted(freq.items(), key=lambda x: (x[1], x[0]))
        unique = len(sorted_freq)
        start = 0
        while start < unique:
            key, val = sorted_freq[start]
            if k - val < 0:
                break
            k -= val
            start += 1
        return unique - start


class SolutionCounter:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = collections.Counter(arr)
        unique = len(freq)
        freq_count = collections.Counter(freq.values())
        for count in range(1, k + 1):
            if k < count * freq_count[count]:
                return unique - k // count
            k -= count*freq_count[count]
            unique -= freq_count[count]
        return unique


if __name__ == '__main__':
    sol = Solution()
    ans = sol.findLeastNumOfUniqueInts([3,3,4], 1)
    print(ans)