from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greaterMap = {}
        decreaseStack = []
        for num in nums2:
            while decreaseStack and num > decreaseStack[-1]:
                prevNum = decreaseStack.pop()
                greaterMap[prevNum] = num
            decreaseStack.append(num)
        answer = []

        for num in nums1:
            if num in greaterMap:
                answer.append(greaterMap[num])
            else:
                answer.append(-1)
        return answer
