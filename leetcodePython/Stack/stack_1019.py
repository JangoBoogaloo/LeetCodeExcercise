from typing import Optional, List

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def buildList(nums: List[int]):
        if not nums:
            return None
        dummy = ListNode()
        curr = dummy
        for num in nums:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        dataList = []
        while head:
            dataList.append(head.val)
            head = head.next
        decreaseStack = []
        result = [0] * len(dataList)
        for i in range(len(dataList)):
            while decreaseStack and dataList[i] > dataList[decreaseStack[-1]]:
                prevIndex = decreaseStack.pop()
                result[prevIndex] = dataList[i]
            decreaseStack.append(i)
        return result









import pytest
target = Solution()

@pytest.mark.parametrize("dataList, expect",
[
    ([], []),
    ([1], [0]),
    ([5, 4], [0, 0]),
    ([2, 1, 5], [5, 5, 0]),
    ([2, 7, 4, 3, 5], [7, 0, 5, 5, 0])
])
def test_checkType(dataList, expect):
    head = ListNode.buildList(dataList)
    assert target.nextLargerNodes(head) == expect