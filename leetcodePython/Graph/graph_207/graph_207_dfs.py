from typing import List


class Solution:
    def _hasCircle(self, course: int, dependencyOf: List[List[int]], visited: set[int], circleStack: set[int]) -> bool:
        if course in circleStack:
            return True
        if course in visited:
            return False
        visited.add(course)
        circleStack.add(course)
        for nextCourse in dependencyOf[course]:
            if self._hasCircle(nextCourse, dependencyOf, visited, circleStack):
                return True
        circleStack.remove(course)
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependencyOf = [[] for _ in range(numCourses)]
        for dst, src in prerequisites:
            dependencyOf[src].append(dst)
        visited = set()
        circleStack = set()
        for course in range(numCourses):
            if self._hasCircle(course, dependencyOf, visited, circleStack):
                return False
        return True








