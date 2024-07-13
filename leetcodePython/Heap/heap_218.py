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

        edge_index_map = {x : i for i, x in enumerate(positions)}
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