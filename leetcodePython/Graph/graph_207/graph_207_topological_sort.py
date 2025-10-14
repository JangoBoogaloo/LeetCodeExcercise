from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependCount = defaultdict(int)
        dependencyOf = [[] for _ in range(numCourses)]
        for dst, src in prerequisites:
            dependencyOf[src].append(dst)
            dependCount[dst] += 1
        noDependQueue = deque()
        for course in range(numCourses):
            if dependCount[course] == 0:
                noDependQueue.append(course)
        courseTaken = 0
        while noDependQueue:
            currCourse = noDependQueue.popleft()
            courseTaken += 1
            for dependCourse in dependencyOf[currCourse]:
                dependCount[dependCourse] -= 1
                if dependCount[dependCourse] == 0:
                    noDependQueue.append(dependCourse)
        return courseTaken == numCourses








