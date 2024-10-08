from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))

        connect_degree = [set() for _ in range(n)]

        for src, dst in edges:
            connect_degree[src].add(dst)
            connect_degree[dst].add(src)

        leaves = []
        for i in range(n):
            if len(connect_degree[i]) == 1:
                leaves.append(i)
        remain = n
        while remain > 2:
            remain -= len(leaves)
            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                parent = connect_degree[leaf].pop()
                connect_degree[parent].remove(leaf)
                if len(connect_degree[parent]) == 1:
                    new_leaves.append(parent)
            leaves = new_leaves

        return leaves
