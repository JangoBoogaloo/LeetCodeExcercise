from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumSemesters(self, numCourses: int, relations: List[List[int]]) -> int:
        dependCount = defaultdict(int)
        dependencyOf = defaultdict(list)
        for src, dst in relations:
            dependencyOf[src].append(dst)
            dependCount[dst] += 1
        noDependQueue = deque()
        for course in range(1, numCourses+1):
            if dependCount[course] == 0:
                noDependQueue.append(course)
        courseTaken = 0
        semesters = 0

        while noDependQueue:
            nonDependCount = len(noDependQueue)
            for _ in range(nonDependCount):
                currCourse = noDependQueue.popleft()
                courseTaken += 1
                for dependCourse in dependencyOf[currCourse]:
                    dependCount[dependCourse] -= 1
                    if dependCount[dependCourse] == 0:
                        noDependQueue.append(dependCourse)
            semesters += 1
        if courseTaken < numCourses:
            return -1
        return semesters









