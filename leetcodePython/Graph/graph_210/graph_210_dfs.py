from typing import List


class Solution:
    def _hasCircle(self, course: int, dependencyOf: List[List[int]], visited: set[int], circleStack: set[int], courses: List[int]) -> bool:
        if course in circleStack:
            return True
        if course in visited:
            return False
        visited.add(course)
        circleStack.add(course)
        for nextCourse in dependencyOf[course]:
            if self._hasCircle(nextCourse, dependencyOf, visited, circleStack, courses):
                return True
        circleStack.remove(course)
        courses.append(course)
        return False
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dependencyOf = [[] for _ in range(numCourses)]
        for dst, src in prerequisites:
            dependencyOf[src].append(dst)
        visited = set()
        circleStack = set()
        courses = []
        for course in range(numCourses):
            if self._hasCircle(course, dependencyOf, visited, circleStack, courses):
                return []
        return courses[::-1]









