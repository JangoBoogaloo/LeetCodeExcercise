from typing import List, Optional
from union_find import DirectedUF

class Solution:
    @staticmethod
    def _findMultiParentEdges(edges: List[List[int]]) -> tuple[Optional[List[int]],Optional[List[int]]]:
        parentOf = [i for i in range(len(edges)+1)]
        multiParentEdge1, multiParentEdge2 = None, None
        for parent, child in edges:
            if parentOf[child] == child:
                parentOf[child] = parent
            else:
                multiParentEdge1 = [parentOf[child], child]
                multiParentEdge2 = [parent, child]
        return multiParentEdge1, multiParentEdge2

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        multiParentEdge1, multiParentEdge2 = self._findMultiParentEdges(edges)
        uf = DirectedUF()
        for parent, child in edges:
            if [parent, child] == multiParentEdge2:
                continue
            uf.add(parent), uf.add(child)
            if uf.find(parent) == uf.find(child):
                if multiParentEdge1:
                    return multiParentEdge1
                return [parent, child]
            uf.union(child, parent)
        return multiParentEdge2









