from typing import List


class Solution:
    @staticmethod
    def _evaluate(x, y, operator):
        if operator == "+":
            return x
        if operator == "-":
            return -x
        if operator == "*":
            return x * y
        if operator == "/":
            return int(x / y)
        raise ValueError(f'operation \'{operator}\' is invalid')

    def calculate(self, s: str) -> int:
        curr_num = 0
        prev_op = '+'
        stack = []
        s += '!'  # just a final sudo OP to make the previous stacked operations complete
        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            elif ch == '(':
                stack.append(prev_op)
                prev_op = '+'
            else:  # it's '+-*/' or ')' or '!'
                if prev_op in '*/':  # mult and div will all be calculated
                    stack.append(self._evaluate(stack.pop(), curr_num, prev_op))
                else:  # plus and sub will all be stacked with sign
                    stack.append(self._evaluate(curr_num, 0, prev_op))
                # reset, previous number is already stacked
                curr_num = 0
                if ch == ')':  # close, sum up all the number in bracket: in stack until we hit an op
                    while type(stack[-1]) == int:
                        curr_num += stack.pop()
                    prev_op = stack.pop()
                else:  # it's '+-*/' or '!'
                    prev_op = ch

        return sum(stack)
