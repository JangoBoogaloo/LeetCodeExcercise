from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        edge1 = None
        edge2 = None

        def find(x) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y) -> bool:
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False
            parent[rootY] = rootX
            return True

        # check for nodes with two parents
        for parentNode, childNode in edges:
            if parent[childNode] != childNode:
                edge1 = [parent[childNode], childNode]
                edge2 = [parentNode, childNode]
            else:
                parent[childNode] = parentNode

        # union find to detect cycles
        parent = [i for i in range(n + 1)]
        for parentNode, childNode in edges:
            # try to skip parent-child edge 2 and see if it still causes cycle
            if [parentNode, childNode] == edge2:
                continue
            # still a cycle, then should be edge1
            if not union(parentNode, childNode):
                if edge1:
                    return edge1
                # no multi parent, simply remove current edge
                return [parentNode, childNode]
        return edge2

