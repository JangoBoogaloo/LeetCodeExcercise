from typing import List


class Solution:
    @staticmethod
    def _seePeopleForRow(row: int, heights: List[List[int]], answer: List[List[int]]) -> None:
        decreaseHeightIndexStack = []
        for i in range(len(heights[row])):
            equal = False
            while decreaseHeightIndexStack and heights[row][i] >= heights[row][decreaseHeightIndexStack[-1]]:
                if heights[row][i] == heights[row][decreaseHeightIndexStack[-1]]:
                    equal = True
                answer[row][decreaseHeightIndexStack[-1]] += 1
                decreaseHeightIndexStack.pop()
            if decreaseHeightIndexStack and not equal:
                answer[row][decreaseHeightIndexStack[-1]] += 1

            decreaseHeightIndexStack.append(i)

    @staticmethod
    def _seePeopleForColumn(col: int, heights: List[List[int]], answer: List[List[int]]) -> None:
        decreaseHeightIndexStack = []
        for i in range(len(heights)):
            equal = False
            while decreaseHeightIndexStack and heights[i][col] >= heights[decreaseHeightIndexStack[-1]][col]:
                if heights[i][col] == heights[decreaseHeightIndexStack[-1]][col]:
                    equal = True
                answer[decreaseHeightIndexStack[-1]][col] += 1
                decreaseHeightIndexStack.pop()
            if decreaseHeightIndexStack and not equal:
                answer[decreaseHeightIndexStack[-1]][col] += 1

            decreaseHeightIndexStack.append(i)
        return

    def seePeople(self, heights: List[List[int]]) -> List[List[int]]:
        answer = [[0]*len(heights[0]) for _ in range(len(heights))]
        for r in range(len(heights)):
            self._seePeopleForRow(r, heights, answer)
        for c in range(len(heights[0])):
            self._seePeopleForColumn(c, heights, answer)

        return answer
