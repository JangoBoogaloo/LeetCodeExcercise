from typing import List
from collections import Counter


class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        free_servers = [0] * len(queries)
        sorted_query_map = sorted((q, i) for i, q in enumerate(queries))
        logs.sort(key=lambda log: log[1])
        left = right = 0
        server_usage = Counter()
        current_free_servers = n
        for end, index in sorted_query_map:
            start = end - x
            while right < len(logs) and logs[right][1] <= end:
                server_id = logs[right][0]
                server_usage[server_id] += 1
                if server_usage[server_id] == 1:
                    current_free_servers -= 1
                right += 1
            while left < len(logs) and logs[left][1] < start:
                server_id = logs[left][0]
                server_usage[server_id] -= 1
                if server_usage[server_id] == 0:
                    current_free_servers += 1
                left += 1
            free_servers[index] = current_free_servers
        return free_servers
