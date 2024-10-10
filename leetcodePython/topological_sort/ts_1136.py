from typing import List


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        indegree = [0] * (n + 1)
        from_to: List[List[int]]
        from_to = [[] for _ in range(n + 1)]
        for src, dst in relations:
            from_to[src].append(dst)
            indegree[dst] += 1

        this_semester = []
        for course in range(n + 1):
            if indegree[course] == 0:
                this_semester.append(course)

        semesters = 0
        while this_semester:
            next_semester = []
            semesters += 1
            for src in this_semester:
                if src == 0:
                    continue
                n -= 1
                for dst in from_to[src]:
                    indegree[dst] -= 1
                    if indegree[dst] == 0:
                        next_semester.append(dst)
            this_semester = next_semester

        if n == 0:
            return semesters
        return -1


if __name__ == "__main__":
    sol = Solution()
    sol.minimumSemesters(3, [[1, 3], [2, 3]])
