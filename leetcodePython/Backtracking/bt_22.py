from typing import List


class Solution:
    left = right = 0

    def generateParenthesis(self, n: int) -> List[str]:
        permutations = []
        current = []
        self.left = self.right = 0

        def backtrack() -> None:
            if len(current) == 2 * n:
                permutations.append("".join(current))
            if self.left < n:
                current.append("(")
                self.left += 1
                backtrack()
                self.left -= 1
                current.pop()

            if self.left > self.right:
                current.append(")")
                self.right += 1
                backtrack()
                self.right -= 1
                current.pop()

        backtrack()
        return permutations
