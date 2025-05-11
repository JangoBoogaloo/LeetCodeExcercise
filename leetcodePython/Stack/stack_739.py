from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        index_stack = []
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while index_stack and temperatures[i] > temperatures[index_stack[-1]]:
                index = index_stack.pop()
                answer[index] = i - index
            index_stack.append(i)

        return answer