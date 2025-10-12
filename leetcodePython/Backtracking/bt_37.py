from typing import List


class Solution:
    _BOARD_SIZE = 9
    _BOX_SIZE = 3
    _EMPTY = "."
    _INDEX_END = _BOARD_SIZE * _BOARD_SIZE
    _DATA_SET = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def __init__(self):
        self._rowNumbers: List[set]
        self._colNumbers: List[set]
        self._boxNumbers: List[List[set]]
        self._board: List[List[str]]
        self._resolved = False

    def _getBoxPos(self, row: int, col: int) -> tuple[int, int]:
        return row//self._BOX_SIZE, col//self._BOX_SIZE

    def _initBoard(self, board: List[List[str]]) -> None:
        self._board = board
        self._resolved = False
        self._rowNumbers = [set(self._DATA_SET) for _ in range(self._BOARD_SIZE)]
        self._colNumbers = [set(self._DATA_SET) for _ in range(self._BOARD_SIZE)]
        self._boxNumbers = [[set(self._DATA_SET) for _ in range(self._BOX_SIZE)] for _ in range(self._BOX_SIZE)]
        for row in range(len(self._board)):
            for col in range(len(self._board[0])):
                number = self._board[row][col]
                if number == self._EMPTY:
                    continue
                self._place(number, row, col)

    def _canPlace(self, number: str, row: int, col: int) -> bool:
        if number not in self._rowNumbers[row]:
            return False
        if number not in self._colNumbers[col]:
            return False
        boxRow, boxCol = self._getBoxPos(row, col)
        if number not in self._boxNumbers[boxRow][boxCol]:
            return False
        return True

    def _place(self, number: str, row: int, col: int):
        boxRow, boxCol = self._getBoxPos(row, col)
        self._rowNumbers[row].remove(number)
        self._colNumbers[col].remove(number)
        self._boxNumbers[boxRow][boxCol].remove(number)
        self._board[row][col] = number

    def _remove(self, number: str, row: int, col: int):
        boxRow, boxCol = self._getBoxPos(row, col)
        self._rowNumbers[row].add(number)
        self._colNumbers[col].add(number)
        self._boxNumbers[boxRow][boxCol].add(number)
        self._board[row][col] = self._EMPTY

    def solveSudoku(self, board: List[List[str]]) -> None:
        self._initBoard(board)

        def backtrack(index: int):
            if index == self._INDEX_END:
                self._resolved = True
                return

            row = index // self._BOARD_SIZE
            col = index % self._BOARD_SIZE
            if self._board[row][col] != self._EMPTY:
                backtrack(index+1)
                return
            for number in self._DATA_SET:
                if not self._canPlace(number, row, col):
                    continue
                # place current step
                self._place(number, row, col)
                # next step
                backtrack(index + 1)
                if self._resolved:
                    return
                # revert current step
                self._remove(number, row, col)

        backtrack(0)
