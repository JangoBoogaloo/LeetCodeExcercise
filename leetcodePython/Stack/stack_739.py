from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        decreaseTempIndex = []
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while decreaseTempIndex and temperatures[i] > temperatures[decreaseTempIndex[-1]]:
                smallTempIndex = decreaseTempIndex.pop()
                answer[smallTempIndex] = i - smallTempIndex
            decreaseTempIndex.append(i)
        return answer
