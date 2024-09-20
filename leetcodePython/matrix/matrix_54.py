from typing import List


class Solution:
    @staticmethod
    def _out_of_bound(rows: int, cols: int, row: int, col: int) -> bool:
        if row < 0 or col < 0:
            return True
        if row >= rows or col >= cols:
            return True
        return False

    def _get_new_pos(self, visited: List[List[bool]], row: int, col: int, direction: List[tuple[int, int]],
                     direction_id: int) -> tuple[int, int, int]:
        for _ in range(len(direction)):
            dr, dc = direction[direction_id]
            nr, nc = row + dr, col + dc
            if self._out_of_bound(len(visited), len(visited[0]), nr, nc) or visited[nr][nc]:
                direction_id = (direction_id + 1) % len(direction)
            else:
                return nr, nc, direction_id
        return -1, -1, direction_id

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # the movement pattern follows: RDLU, when we hit a visited location, we change our direction.
        # When we visited all we stop.
        rows, cols = len(matrix), len(matrix[0])
        visited = [[False] * cols for _ in range(rows)]
        un_visit_count = rows * cols
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_id = 0
        row, col = 0, 0
        path = []
        while un_visit_count > 0:
            path.append(matrix[row][col])
            visited[row][col] = True
            un_visit_count -= 1
            row, col, direction_id = self._get_new_pos(visited, row, col, direction, direction_id)
        return path


if __name__ == "__main__":
    sol = Solution()
    ans = sol.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(ans)
