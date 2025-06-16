from collections import defaultdict


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        charAt = defaultdict(list)
        direction = 1
        row = 0
        charList = list(s)
        for ch in charList:
            charAt[row].append(ch)
            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1
            row += direction
        rows = []
        for row in range(numRows):
            rows.append("".join(charAt[row]))
        return "".join(rows)