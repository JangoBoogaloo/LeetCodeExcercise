from typing import List


class SolutionBruteForce:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        for start in range(len(nums)):
            curr_sum = 0
            for end in range(start, len(nums)):
                curr_sum += nums[end]
                sums.append(curr_sum)
        sums.sort()
        return sum(sums[left-1:right]) % (10**9 + 7)


if __name__ == "__main__":
    sol = SolutionBruteForce()
    ans = sol.rangeSum([1,2,3,4], 4, 3, 4)
    print(ans)