import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        from_to: List[List[int]]
        from_to = [[] for _ in range(numCourses)]
        for src, dst in prerequisites:
            from_to[src].append(dst)
            indegree[dst] += 1

        queue = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        visited = 0
        while queue:
            src = queue.popleft()
            visited += 1
            for dst in from_to[src]:
                indegree[dst] -= 1
                if indegree[dst] == 0:
                    queue.append(dst)
        return visited == numCourses