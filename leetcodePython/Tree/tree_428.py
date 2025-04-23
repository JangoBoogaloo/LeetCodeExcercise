from typing import Optional, List
from collections import deque


class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children


class Codec:
    _PARENT_SEPARATOR = "|"
    _NODE_SEPARATOR = ","
    _NULL = "X"

    def serialize(self, root: Node) -> str:
        if not root:
            return self._NULL
        levelQueue: deque[Node] = deque()
        nodeStrList = []
        levelQueue.append(root)
        nodeStrList.append(self._formatNode(root.val, -1))
        parentIndex = 1
        while levelQueue:
            for i in range(len(levelQueue)):
                parent = levelQueue.popleft()
                for child in parent.children:
                    levelQueue.append(child)
                    nodeStr = self._formatNode(child.val, parentIndex)
                    nodeStrList.append(nodeStr)
                parentIndex += 1
        return f"{self._NODE_SEPARATOR}".join(nodeStrList)

    def deserialize(self, data: str) -> Optional[Node]:
        if data == self._NULL:
            return None
        nodeStrList = data.split(self._NODE_SEPARATOR)
        parentNodes = [None]
        for nodeStr in nodeStrList:
            nodeDataStr, parentStr = nodeStr.split(self._PARENT_SEPARATOR)
            nodeData = int(nodeDataStr)
            current = Node(nodeData)
            parentNodes.append(current)
            if parentStr != self._NULL:
                parentPos = int(parentStr)
                parentNodes[parentPos].children.append(current)
        return parentNodes[1]

    def _formatNode(self, nodeValue: int, parentIndex: int) -> str:
        parentIndexStr = parentIndex
        if parentIndex == -1:
            parentIndexStr = self._NULL
        return f"{nodeValue}{self._PARENT_SEPARATOR}{parentIndexStr}"
