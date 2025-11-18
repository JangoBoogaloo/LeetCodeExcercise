from collections import defaultdict
from typing import List


class Solution:
    _OPERATIONS = {"+", "-", "*"}

    @staticmethod
    def _calculate(num1, num2, op) -> int:
        match op:
            case '+':
                return num1 + num2
            case '-':
                return num1 - num2
            case '*':
                return num1 * num2
        return -1

    def _evaluate(self, expression, resultOf) -> List[int]:
        if expression in resultOf:
            return resultOf[expression]

        if expression.isdigit():
            resultOf[expression] = [int(expression)]
            return resultOf[expression]

        for i, ch in enumerate(expression):
            if ch not in self._OPERATIONS:
                continue
            leftResults = self._evaluate(expression[:i], resultOf)
            rightResults = self._evaluate(expression[i+1:], resultOf)
            for leftResult in leftResults:
                for rightResult in rightResults:
                    answer = self._calculate(leftResult, rightResult, ch)
                    resultOf[expression].append(answer)
        return resultOf[expression]


    def diffWaysToCompute(self, expression: str) -> List[int]:
        resultOf = defaultdict(list)
        return self._evaluate(expression, resultOf)