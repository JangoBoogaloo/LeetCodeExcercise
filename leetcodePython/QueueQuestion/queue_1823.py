import collections


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = collections.deque(list(range(1, n + 1)))
        while len(circle) > 1:
            for _ in range(k-1):
                current = circle.popleft()
                circle.append(current)
            circle.popleft()
        return circle[0]


if __name__ == "__main__":
    solution = Solution()
    print(solution.findTheWinner(6, 5))