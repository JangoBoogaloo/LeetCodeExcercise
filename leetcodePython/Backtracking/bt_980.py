from typing import List


class Solution:
    @staticmethod
    def _can_walk(grid: List[List[int]], row: int, col: int) -> bool:
        if row < 0 or row >= len(grid):
            return False
        if col < 0 or col >= len(grid[0]):
            return False
        if grid[row][col] == -1:
            return False
        return True

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        walks = []
        path: List[tuple[int, int]] = []
        empty = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    empty += 1
                if grid[r][c] == 1:
                    visited[r][c] = True
                    path.append((r, c))

        def backtrack(remain: int):
            row, col = path[-1]
            if grid[row][col] == 2 and remain == -1:
                walks.append(path[:])
                return

            for r, c in directions:
                new_row, new_col = row + r, col + c
                if not self._can_walk(grid, new_row, new_col) or visited[new_row][new_col]:
                    continue
                visited[new_row][new_col] = True
                path.append((new_row, new_col))
                backtrack(remain-1)
                path.pop()
                visited[new_row][new_col] = False
        backtrack(empty)
        print(walks)
        return len(walks)


if __name__ == "__main__":
    sol = Solution()
    ans = sol.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]])
    print(ans)