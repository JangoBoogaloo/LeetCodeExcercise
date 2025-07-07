from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        smallerDataIndexStack = []
        subArrayEndAtIndexMinSum = [0] * len(arr)
        for i, data in enumerate(arr):
            while smallerDataIndexStack and arr[smallerDataIndexStack[-1]] >= arr[i]:
                smallerDataIndexStack.pop()

            if smallerDataIndexStack:
                smaller_index = smallerDataIndexStack[-1]
                subArrayEndAtIndexMinSum[i] = subArrayEndAtIndexMinSum[smaller_index] + (i-smaller_index) * arr[i]
            else:
                subArrayEndAtIndexMinSum[i] = (i + 1) * arr[i]
            smallerDataIndexStack.append(i)
        return sum(subArrayEndAtIndexMinSum) % MOD


class SolutionBruteForce:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        subArrayMinSum = 0
        for right in range(len(arr)):
            for left in range(right + 1):
                minNum = min(arr[left:right + 1])
                subArrayMinSum += minNum
        return subArrayMinSum
