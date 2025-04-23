from typing import List


class Solution:
    _DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def _pos_valid(self, pos: tuple[int, int], visited: List[List[bool]]) -> bool:
        pos_x, pos_y = pos
        if pos_x < 0 or pos_x > len(visited[0]) - 1:
            return False
        if pos_y < 0 or pos_y > len(visited) - 1:
            return False
        if visited[pos_y][pos_x]:
            return False
        return True

    def _word_start_at(self, pos: tuple[int, int], word: str, board: List[List[str]],
                       visited: List[List[bool]]) -> bool:
        if len(word) == 0:
            return True
        pos_x, pos_y = pos
        for move_x, move_y in self._DIRECTIONS:
            new_x = pos_x + move_x
            new_y = pos_y + move_y
            if not self._pos_valid((new_x, new_y), visited):
                continue
            visited[new_y][new_x] = True
            if board[new_y][new_x] == word[0] and self._word_start_at((new_x, new_y), word[1:], board, visited):
                return True
            visited[new_y][new_x] = False
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        for y in range(len(board)):
            for x in range(len(board[0])):
                visited[y][x] = True
                if board[y][x] == word[0] and self._word_start_at((x, y), word[1:], board, visited):
                    return True
                visited = [[False] * len(board[0]) for _ in range(len(board))]
        return False
