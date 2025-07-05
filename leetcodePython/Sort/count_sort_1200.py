from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minVal = min(arr)
        maxVal = max(arr)
        countAtDiff = [0] * (maxVal - minVal + 1)
        for num in arr:
            countAtDiff[num-minVal] = 1

        answer = []
        minDiff = maxVal - minVal
        prevDiff = 0
        for diff in range(1, maxVal - minVal + 1):
            if countAtDiff[diff] == 0:
                continue

            if diff - prevDiff == minDiff:
                currNum = diff + minVal
                prevNum = prevDiff + minVal
                answer.append([prevNum, currNum])
            elif diff - prevDiff < minDiff:
                currNum = diff + minVal
                prevNum = prevDiff + minVal
                answer = [[prevNum, currNum]]
                minDiff = currNum - prevNum
            prevDiff = diff
        return answer
