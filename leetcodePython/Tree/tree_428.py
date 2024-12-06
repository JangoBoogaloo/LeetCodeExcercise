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
        data_str_list = []
        queue = deque()
        queue.append(root)
        data_str_list.append(f"{root.val}{self._PARENT_SEPARATOR}{self._NULL}{self._NODE_SEPARATOR}")
        parent_index = 1
        while queue:
            for i in range(len(queue)):
                parent = queue.popleft()
                for j in range(len(parent.children)):
                    queue.append(parent.children[j])
                    data_str_list.append(
                        f"{parent.children[j].val}{self._PARENT_SEPARATOR}{parent_index}{self._NODE_SEPARATOR}")
                parent_index += 1
        return "".join(data_str_list)[:-1]

    def deserialize(self, data: str) -> Optional[Node]:
        if data == self._NULL:
            return None
        node_str_list = data.split(self._NODE_SEPARATOR)
        node_list = [None]
        for node_str in node_str_list:
            value_str, parent_str = node_str.split(self._PARENT_SEPARATOR)
            parent_pos = 0
            if parent_str != self._NULL:
                parent_pos = int(parent_str)
            val = int(value_str)
            curr_node = Node(val)
            node_list.append(curr_node)
            if not node_list[parent_pos]:
                continue
            node_list[parent_pos].children.append(curr_node)
        return node_list[1]
