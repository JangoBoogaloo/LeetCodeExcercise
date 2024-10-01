from typing import List


class Solution:
    """
    books[r]+(books[r]−1)+(books[r]−2) + ⋯ +(books[r]−(count−1))
    """
    @staticmethod
    def _calculateSum(books: List[int], left: int, right: int) -> int:
        # books[right] - (count - 1) > 0
        # books[right] >= count
        count = min(books[right], right - left + 1)
        left_data = books[right] - (count - 1)
        right_data = books[right]
        return (left_data + right_data) * count // 2

    def maximumBooks(self, books: List[int]) -> int:
        size = len(books)
        stack = []
        dp = [0] * size
        for right in range(size):
            while stack:
                left = stack[-1]
                # books[j] < books[i]−(i−j)
                # if we can't form a strictly 1 diff increasing sequence between left and right, now this is smaller, we keep stack
                if books[left] < books[right] - (right - left):
                    break
                stack.pop()
            if not stack:
                dp[right] = self._calculateSum(books, 0, right)
            else:
                # guarantee data at index left is smaller than the 1 diff sequence
                left = stack[-1]
                # now the sum becomes whatever sum the left can form and the sum formed by left + 1 to right
                dp[right] = dp[left] + self._calculateSum(books, left + 1, right)
            stack.append(right)
        return max(dp)


if __name__ == "__main__":
    sol = Solution()
    ans = sol.maximumBooks([2, 7, 5, 4])