from typing import List


class Solution:
    @staticmethod
    def evaluate(x, y, operator):
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
                if prev_op in '*/':
                    stack.append(self.evaluate(stack.pop(), curr_num, prev_op))
                else:
                    stack.append(self.evaluate(curr_num, 0, prev_op))
                curr_num = 0
                if ch == ')':
                    while type(stack[-1]) == int:
                        curr_num += stack.pop()
                    prev_op = stack.pop()
                else:  # it's '+-*/' or '!'
                    prev_op = ch

        return sum(stack)
