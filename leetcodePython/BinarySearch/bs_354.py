import bisect
from typing import List


class Solution:
    @staticmethod
    def _lengthOfLIS(nums: List[int]) -> int:
        sequence = []
        for num in nums:
            idx = bisect.bisect_left(sequence, num)
            if idx == len(sequence):
                sequence.append(num)
            else:
                sequence[idx] = num
        return len(sequence)

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # when width is same, we make height in reverse order, so width same data can not form increasing sequence for height at all.
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        height_array = [data[1] for data in envelopes]
        return self._lengthOfLIS(height_array)

if __name__ == '__main__':
    sol = Solution()
    ans = sol.maxEnvelopes([[1,1],[1,2],[2,3]])
    print(ans)