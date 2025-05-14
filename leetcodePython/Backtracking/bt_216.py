from typing import List


class Solution:
    current_sum = 0

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combinations = []
        current = []
        self.current_sum = 0

        def backtrack(start: int):
            if len(current) > k or self.current_sum > n:
                return
            if self.current_sum == n and len(current) == k:
                combinations.append(current[:])
                return
            for num in range(start, 10):
                self.current_sum += num
                current.append(num)
                backtrack(num + 1)
                self.current_sum -= num
                current.pop()

        backtrack(1)
        return combinations


if __name__ == "__main__":
    sol = Solution()
    ans = sol.combinationSum3(9, 45)
    print(ans)
