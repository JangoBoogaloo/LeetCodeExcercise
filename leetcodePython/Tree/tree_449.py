from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    _NODE_SEPARATOR = ","
    _INFO_SEPARATOR = "|"
    _LEFT = "L"
    _RIGHT = "R"
    _ROOT = "O"
    _NULL = "X"

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        parents = deque()
        node_str_list = []
        # "1|O|X,2|L|0,3|R|0,4|L|1,5|R|1"
        node_str = f"{root.val}{self._INFO_SEPARATOR}{self._ROOT}{self._INFO_SEPARATOR}{self._NULL}{self._NODE_SEPARATOR}"
        node_index = 0
        node_str_list.append(node_str)
        parents.append(root)
        while parents:
            count = len(parents)
            for i in range(count):
                parent = parents.popleft()
                if parent.left:
                    node = parent.left
                    node_str = f"{node.val}{self._INFO_SEPARATOR}{self._LEFT}{self._INFO_SEPARATOR}{node_index}{self._NODE_SEPARATOR}"
                    node_str_list.append(node_str)
                    parents.append(node)
                if parent.right:
                    node = parent.right
                    node_str = f"{node.val}{self._INFO_SEPARATOR}{self._RIGHT}{self._INFO_SEPARATOR}{node_index}{self._NODE_SEPARATOR}"
                    node_str_list.append(node_str)
                    parents.append(node)
                node_index += 1
        return "".join(node_str_list)[:-1]

    def _deserializeNode(self, node_list: List[TreeNode], node_str:str) -> None:
        value_str, type_str, root_index_str = node_str.split(self._INFO_SEPARATOR)
        value = int(value_str)
        node = TreeNode(value)
        if type_str == self._ROOT:
            node_list.append(node)
            return

        parent = node_list[int(root_index_str)]
        if type_str == self._LEFT:
            parent.left = node
        else:
            parent.right = node
        node_list.append(node)
        return

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        node_list = []
        node_str_list = data.split(self._NODE_SEPARATOR)
        for node_str in node_str_list:
            self._deserializeNode(node_list, node_str)
        return node_list[0]
