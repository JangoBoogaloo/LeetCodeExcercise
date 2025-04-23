from typing import List


class SolutionBacktrack:
    _max_request: int

    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        change_in_building = [0] * n
        self._max_request = 0

        def backtrack(request_index: int, request_counted: int) -> None:
            if request_index == len(requests):
                if min(change_in_building) < 0:
                    return
                self._max_request = max(self._max_request, request_counted)
                return
            src, dst = requests[request_index]

            change_in_building[src] -= 1
            change_in_building[dst] += 1
            backtrack(request_index + 1, request_counted + 1)

            change_in_building[src] += 1
            change_in_building[dst] -= 1
            backtrack(request_index + 1, request_counted)

        backtrack(0, 0)
        return self._max_request


from itertools import combinations


class SolutionPythonCombination:
    def maximumRequests(self, n: int, requests: List[List[int]]) ->int:
        max_req = 0
        for k in range(len(requests), 0, -1):
            for subset in combinations(requests, k):
                balance = [0] * n
                for frm, to in subset:
                    balance[frm] -= 1
                    balance[to] += 1
                if all(b == 0 for b in balance):
                    return k
        return 0
