from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        current_path = [0]

        def backtrack(src_index: int) -> None:
            if src_index == len(graph) - 1:
                paths.append(current_path[:])
                return
            destinations = graph[src_index]
            for dst_index in destinations:
                current_path.append(dst_index)
                backtrack(dst_index)
                current_path.pop()

        backtrack(0)
        return paths


if __name__ == "__main__":
    sol = Solution()
    ans = sol.allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []])
    print(ans)
