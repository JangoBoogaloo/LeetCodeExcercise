from typing import List
from heapq import *


class Solution:
    @staticmethod
    def _pop_ended_pos_height(height_end_i_heap: List[tuple[int,int]], edge_pos: int):
        while height_end_i_heap and height_end_i_heap[0][1] <= edge_pos:
            heappop(height_end_i_heap)

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        building_edges = []
        for i, (start_i, end_i, _) in enumerate(buildings):
            building_edges.append((start_i, i))
            building_edges.append((end_i, i))
        building_edges.sort()

        height_end_i_heap = []
        ans = []
        i = 0
        while i < len(building_edges):
            curr_pos = building_edges[i][0]

            while i < len(building_edges) and building_edges[i][0] == curr_pos:
                building_i = building_edges[i][1]
                start_pos = buildings[building_i][0]
                if start_pos == curr_pos:
                    _, end_pos, height = buildings[building_i]
                    heappush(height_end_i_heap, [-height, end_pos])
                self._pop_ended_pos_height(height_end_i_heap, curr_pos)
                i += 1

            if height_end_i_heap:
                max_height = -height_end_i_heap[0][0]
            else:
                max_height = 0

            if not ans:
                ans.append([curr_pos, max_height])
                continue
            last_height = ans[-1][1]
            if max_height != last_height:
                ans.append([curr_pos, max_height])
        return ans


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
