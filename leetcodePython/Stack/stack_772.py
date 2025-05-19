from typing import List


class Solution:

    _OPERATIONS = {"+", "-", "*", "/"}

    @staticmethod
    def _operateAppend(num: int, operator: str, stack: List[int]) -> None:
        if operator == "+":
            stack.append(num)
        elif operator == "-":
            stack.append(-num)
        elif operator == "*":
            stack.append(stack.pop()*num)
        elif operator == "/":
            stack.append(int(stack.pop()/num))
        else:
            raise ValueError(f'operation \'{operator}\' is invalid')

    def _calculateAndJump(self, index: int, equation: str) -> tuple[int, int]:
        curr_num = 0
        stack = []
        operation = "+"
        while index < len(equation):
            ch = equation[index]
            if ch.isdigit():
                curr_num = 10 * curr_num + int(ch)
            elif ch in self._OPERATIONS:
                self._operateAppend(curr_num, operation, stack)
                curr_num = 0
                operation = ch
            elif ch == "(":
                curr_num, index = self._calculateAndJump(index+1, equation)
            elif ch == ")":
                self._operateAppend(curr_num, operation, stack)
                return sum(stack), index
            index += 1
        return sum(stack), 0

    def calculate(self, s: str) -> int:
        result, _ = self._calculateAndJump(0, s+"+")
        return result
