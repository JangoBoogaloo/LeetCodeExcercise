from typing import List


class SolutionBruteForce:
    def _getRange(self, nums: List[int]) -> int:
        return max(nums) - min(nums)

    def subArrayRanges(self, nums: List[int]) -> int:
        sumRange = 0
        for end in range(len(nums)):
            for start in range(end+1):
                sumRange += self._getRange(nums[start:end+1])
        return sumRange


if __name__ == '__main__':
    sol = SolutionBruteForce()
    ans = sol.subArrayRanges([4,-2,-3,4,1])
    print(ans)