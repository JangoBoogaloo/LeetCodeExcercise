from typing import List


class SolutionBruteForce:
    def _climb(self, i: int, n: int) -> int:
        if i > n:
            return 0
        if i == n:
            return 1
        return self._climb(i + 1, n) + self._climb(i + 2, n)

    def climbStairs(self, n: int) -> int:
        return self._climb(0, n)


class SolutionDPTopDown:
    def _climb(self, i: int, n: int, memo: List[int]) -> int:
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] > 0:
            return memo[i]

        memo[i] = self._climb(i + 1, n, memo) + self._climb(i + 2, n, memo)
        return memo[i]

    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)
        return self._climb(0, n, memo)


class SolutionDPBottomUp:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        f_n_prev_prev = 1
        f_n_prev = 2
        for i in range(3, n + 1):
            # f_n-1 take a 1 step
            # f_n-2 take a 2 step
            # f_n = f_n-1 + f_n-2
            f_n = f_n_prev + f_n_prev_prev
            f_n_prev_prev = f_n_prev
            f_n_prev = f_n
        return f_n_prev

