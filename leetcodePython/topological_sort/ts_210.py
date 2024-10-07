import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        from_to: List[List[int]]
        from_to = [[] for _ in range(numCourses)]
        for dst, src, in prerequisites:
            from_to[src].append(dst)
            indegree[dst] += 1

        queue = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        visited = 0
        course = []
        while queue:
            src = queue.popleft()
            course.append(src)
            visited += 1
            for dst in from_to[src]:
                indegree[dst] -= 1
                if indegree[dst] == 0:
                    queue.append(dst)
        if visited == numCourses:
            return course
        return []


if __name__ == "__main__":
    sol = Solution()
    ans = sol.findOrder(2, [[1,0]])
    print(ans)