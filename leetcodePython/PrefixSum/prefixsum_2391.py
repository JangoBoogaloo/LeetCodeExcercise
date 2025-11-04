from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        last_garbage_index = {'P':-1, 'G': -1, 'M': -1}
        garbage_collection_time = 0
        for i, g in enumerate(garbage):
            garbage_collection_time += len(g)
            for ch in g:
                last_garbage_index[ch] = i

        travel_prefix_sum = []
        run_sum = 0
        for t in travel:
            run_sum += t
            travel_prefix_sum.append(run_sum)

        travel_time = 0
        for ch in "PGM":
            if last_garbage_index[ch] > 0:
                travel_time += travel_prefix_sum[last_garbage_index[ch]-1]

        return travel_time + garbage_collection_time










