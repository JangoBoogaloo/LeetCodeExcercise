from typing import List
from collections import Counter

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        result = [0] * len(queries)

        query_map = sorted((time, index) for time, index in enumerate(queries))

        # sort the logs base on request time
        logs.sort(key=lambda l: l[1])
        left = right = 0
        server_usage = Counter()
        available_server = n
        for max_time, index in query_map:
            min_time = max_time - x
            while right < len(logs) and logs[right][1] <= max_time:
                id = logs[right][0]
                if server_usage[id] == 0:
                    available_server -= 1
                server_usage[id] += 1
                right += 1
            while left < len(logs) and logs[left][1] < min_time:
                id = logs[left][0]
                server_usage[id] -= 1
                if server_usage[id] == 0:
                    available_server += 1
                left += 1
            result[index] = available_server
        return result