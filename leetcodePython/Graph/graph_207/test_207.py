import pytest

from Graph.graph_207 import graph_207_dfs

sol1 = graph_207_dfs.Solution()

testCases = [
    (3, [[0, 1], [1, 2], [2, 0]], False),
    (3, [[1, 0], [2, 1]], True),
    (4, [[1, 3], [2, 1], [3, 2], [1, 0]], False),
    (4, [[3, 1], [3, 2], [2, 1], [2, 0], [1, 0]], True),
]

@pytest.mark.parametrize("numCourses, prerequisites, expect", testCases)
def test_canFinish(numCourses, prerequisites, expect):
    assert sol1.canFinish(numCourses, prerequisites) == expect


from Graph.graph_207 import graph_207_topological_sort

sol2 = graph_207_topological_sort.Solution()

@pytest.mark.parametrize("numCourses, prerequisites, expect", testCases)
def test_canFinish(numCourses, prerequisites, expect):
    assert sol2.canFinish(numCourses, prerequisites) == expect