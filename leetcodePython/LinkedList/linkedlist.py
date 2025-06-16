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

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def buildList(nums: List[int]):
        if not nums:
            return None
        dummy = Node()
        curr = dummy
        for num in nums:
            curr.next = Node(num)
            curr = curr.next
        return dummy.next

class CircularList:
    @staticmethod
    def buildCircular(dataList) -> Optional[Node]:
        if not dataList:
            return None
        dummyHead = Node()
        current = dummyHead
        for data in dataList:
            current.next = Node(data)
            current = current.next
        current.next = dummyHead.next
        dummyHead.next = None
        del dummyHead
        return current.next

    @staticmethod
    def GetList(node: Optional[Node]):
        if not node:
            return []
        head = node
        dataList = [node.val]
        node = node.next
        while node != head:
            dataList.append(node.val)
            node = node.next
        return dataList


import pytest
circularList = CircularList()

@pytest.mark.parametrize("dataList",
[
    ([]),
    ([1]),
    ([1, 2]),
])
def test_CircularList(dataList):
    node = CircularList.buildCircular(dataList)
    assert CircularList.GetList(node) == dataList