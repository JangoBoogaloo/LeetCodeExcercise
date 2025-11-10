from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReqCount = defaultdict(int)
        dependencyOf = [[] for _ in range(numCourses)]
        for dst, src in prerequisites:
            dependencyOf[src].append(dst)
            preReqCount[dst] += 1
        readyToTake = deque()
        for course in range(numCourses):
            if preReqCount[course] == 0:
                readyToTake.append(course)

        takenCourses = []
        while readyToTake:
            course = readyToTake.popleft()
            takenCourses.append(course)
            for nextCourse in dependencyOf[course]:
                preReqCount[nextCourse] -= 1
                if preReqCount[nextCourse] == 0:
                    readyToTake.append(nextCourse)
        if len(takenCourses) == numCourses:
            return takenCourses
        return []








