from collections import defaultdict, deque
from typing import List


class Solution:
    _RED = 0
    _BLUE = 1

    @staticmethod
    def _buildPath(edges: List[List[int]], color, edgeMap: defaultdict):
        for src, dst in edges:
            edgeMap[src].append((dst, color))

    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        path = defaultdict(list)
        self._buildPath(redEdges, self._RED, path)
        self._buildPath(blueEdges, self._BLUE, path)
        answer = [float('inf')] * n
        visited = set()
        nodesAvailable = deque([(0, self._RED), (0, self._BLUE)])
        level = 0
        while nodesAvailable:
            nodeCount = len(nodesAvailable)
            for _ in range(nodeCount):
                node, color = nodesAvailable.popleft()
                answer[node] = min(answer[node], level)
                for nextNode, pathColor in path[node]:
                    if color == pathColor or (nextNode, pathColor) in visited:
                        continue
                    visited.add((nextNode, pathColor))
                    nodesAvailable.append((nextNode, pathColor))
            level += 1
        return [d if d != float("inf") else -1 for d in answer]