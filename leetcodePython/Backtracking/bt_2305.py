from typing import List


class SolutionBackTrack:
    unfairness = float("inf")

    def distributeCookies(self, cookies: List[int], k: int) -> float | int:
        distributions = [0] * k
        self.unfairness = float("inf")

        def backtrack_unfair(cooky_index: int, zeros: int) -> float | int:
            if len(cookies) - cooky_index < zeros:
                return float("inf")

            if cooky_index == len(cookies):
                unfair = max(distributions)
                return unfair
            for i in range(k):
                if distributions[i] == 0:
                    zeros -= 1
                distributions[i] += cookies[cooky_index]

                unfair = backtrack_unfair(cooky_index + 1, zeros)
                self.unfairness = min(self.unfairness, unfair)

                distributions[i] -= cookies[cooky_index]
                if distributions[i] == 0:
                    zeros += 1
            return self.unfairness

        backtrack_unfair(0, k)
        return self.unfairness


class SolutionBinarySearch:

    def distribute_in_limit(self, limit: int, cooky_index: int, distribution: List[int], cookies: List[int]) -> bool:
        if cooky_index == len(cookies):
            return True
        for i in range(len(distribution)):
            if distribution[i] + cookies[cooky_index] > limit:
                continue
            distribution[i] += cookies[cooky_index]
            if self.distribute_in_limit(limit, cooky_index + 1, distribution, cookies):
                return True
            distribution[i] -= cookies[cooky_index]

        return False

    def distributeCookies(self, cookies: List[int], k: int) -> float | int:
        left, right = min(cookies), sum(cookies)
        while left < right:
            distribution = [0 for _ in range(k)]
            guess_unfair = (left + right) // 2
            if not self.distribute_in_limit(guess_unfair, 0, distribution, cookies):
                left = guess_unfair + 1
            else:
                right = guess_unfair
        return left
