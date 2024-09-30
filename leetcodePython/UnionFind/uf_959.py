from typing import List


class SolutionGridExpansion:

    def regionsBySlashes(self, grid):
        expanded_grid = self._expand_grid(grid)
        grid_size = len(expanded_grid)
        region_count = 0
        # Count regions using flood fill
        for i in range(grid_size):
            for j in range(grid_size):
                # If we find an unvisited cell (0), it's a new region
                if expanded_grid[i][j] == 0:
                    # Fill that region
                    self._flood_fill(expanded_grid, i, j)
                    region_count += 1

        return region_count

    @staticmethod
    def _expand_grid(grid: List[List[int]]) -> List[List[int]]:
        grid_size = len(grid)
        # Create a 3x3 matrix for each cell in the original grid
        expanded_grid = [[0] * (grid_size * 3) for _ in range(grid_size * 3)]

        # Populate the expanded grid based on the original grid
        # 1 represents a barrier in the expanded grid
        for i in range(grid_size):
            for j in range(grid_size):
                base_row = i * 3
                base_col = j * 3
                # Check the character in the original grid
                if grid[i][j] == "\\":
                    # Mark diagonal for backslash
                    expanded_grid[base_row][base_col] = 1
                    expanded_grid[base_row + 1][base_col + 1] = 1
                    expanded_grid[base_row + 2][base_col + 2] = 1
                elif grid[i][j] == "/":
                    # Mark diagonal for forward slash
                    expanded_grid[base_row][base_col + 2] = 1
                    expanded_grid[base_row + 1][base_col + 1] = 1
                    expanded_grid[base_row + 2][base_col] = 1
        return expanded_grid

    # Flood fill algorithm to mark all cells in a region
    def _flood_fill(self, expanded_grid, row, col):
        # Directions for traversal: right, left, down, up
        DIRECTIONS = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]
        queue = [(row, col)]
        expanded_grid[row][col] = 1

        while queue:
            current_cell = queue.pop(0)
            # Check all four directions from the current cell
            for direction in DIRECTIONS:
                new_row = direction[0] + current_cell[0]
                new_col = direction[1] + current_cell[1]
                # If the new cell is valid and unvisited, mark it and add to queue
                if self._is_valid_cell(expanded_grid, new_row, new_col):
                    expanded_grid[new_row][new_col] = 1
                    queue.append((new_row, new_col))

    @staticmethod
    def _is_valid_cell(expanded_grid, row, col):
        n = len(expanded_grid)
        if row < 0 or col < 0:
            return False
        if row >= n or col >= n:
            return False
        if expanded_grid[row][col] == 1:
            return False
        return True


class SolutionDotsUF:

    def _is_point_boarder(self, side_points: int, point_r: int, point_c: int) -> bool:
        if point_r == 0 or point_c == 0 or point_r == side_points - 1 or point_c == side_points - 1:
            return True

    def regionsBySlashes(self, grid):
        grid_size = len(grid)
        side_points = grid_size + 1
        total_points = side_points * side_points
        uf = UF(total_points)
        for point_r in range(side_points):
            for point_c in range(side_points):
                if self._is_point_boarder(side_points, point_r, point_c):
                    point_id = point_r * side_points + point_c
                    uf.register_parent(point_id, 0)

        uf.register_parent(0, -1)
        # border together form a component
        components = 1
        for r in range(grid_size):
            for c in range(grid_size):
                if grid[r][c] == "/":
                    # connect bottom left with top right
                    top_right = r * side_points + c + 1
                    bottom_left = (r+1) * side_points + c
                    # a circle is formed
                    if not uf.union(top_right, bottom_left):
                        components += 1
                elif grid[r][c] == "\\":
                    # connect top left with bottom right
                    top_left = r * side_points + c
                    bottom_right = (r+1) * side_points + c + 1
                    # a circle is formed
                    if not uf.union(top_left, bottom_right):
                        components += 1
        return components


class UF:
    def __init__(self, size: int):
        self.parents = [-1] * size

    def register_parent(self, a: int, parent: int) -> None:
        self.parents[a] = parent

    def find(self, a: int) -> int:
        if self.parents[a] == -1:
            return a
        self.parents[a] = self.find(self.parents[a])
        return self.parents[a]

    def union(self, a: int, b: int) -> bool:
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False
        self.parents[root_b] = root_a
        return True
