from typing import List


class SolutionBruteForce:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        # get and sort all the building edges
        building_edges = set()
        for building in buildings:
            left, right = building[0], building[1]
            building_edges.add(left)
            building_edges.add(right)
        positions = sorted(list(building_edges))

        edge_index_map = {x: i for i, x in enumerate(positions)}
        position_heights = [0] * len(positions)

        for building in buildings:
            left, right, building_height = building[0], building[1], building[2]
            left_x = edge_index_map[left]
            right_x = edge_index_map[right]
            for x in range(left_x, right_x):
                position_heights[x] = max(position_heights[x], building_height)

        ans = []

        for i in range(len(position_heights)):
            curr_height = position_heights[i]
            curr_x = positions[i]
            # curr height is different from last height, a new key point
            if not ans or ans[-1][1] != curr_height:
                ans.append([curr_x, curr_height])
        return ans


class SolutionBruteForceSweepLine:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Collect and sort the unique positions of all the edges.
        positions = sorted(list(set([x for building in buildings for x in building[:2]])))
        ans = []
        for pos in positions:
            max_height = 0
            for left_pos, right_pos, height in buildings:
                if left_pos <= pos < right_pos:
                    max_height = max(max_height, height)
            if not ans or max_height != ans[-1][1]:
                ans.append([pos, max_height])
        return ans


from heapq import *


class SolutionSweepLinePriorityQueue:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        edges = []
        # again, sort edges
        for i, building in enumerate(buildings):
            edges.append([building[0], i])
            edges.append([building[1], i])
        edges.sort()

        heap = []
        ans = []
        i = 0
        while i < len(edges):
            edge_pos = edges[i][0]
            while i < len(edges) and edges[i][0] == edge_pos:
                building_index = edges[i][1]
                left = buildings[building_index][0]
                if edge_pos == left:
                    right = buildings[building_index][1]
                    height = buildings[building_index][2]
                    heappush(heap, [-height, right])
                while heap and heap[0][1] <= edge_pos:
                    heappop(heap)
                i += 1
            if heap:
                max_height = -heap[0][0]
            else:
                max_height = 0
            if not ans or max_height != ans[-1][1]:
                ans.append([edge_pos, max_height])
        return ans
