import math


class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = 0
        for num in range(1, n + 1):
            total_sum += num
        run_sum = 0
        for num in range(1, n + 1):
            run_sum += num
            right_sum = total_sum - run_sum + num
            if run_sum == right_sum:
                return num
        return -1


class SolutionMath:
    def pivotInteger(self, n: int) -> int:
        sum = (n * (n + 1) // 2)
        pivot = int(math.sqrt(sum))
        return pivot if pivot * pivot == sum else -1


if __name__ == "__main__":
    sol = Solution()
    sol.pivotInteger(8)
