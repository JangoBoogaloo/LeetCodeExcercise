from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        year_population_change = [0] * 2051
        for l in logs:
            year_population_change[l[0]] += 1
            year_population_change[l[1]] -= 1
        max_population = year_population = 0
        max_year = 0
        for year in range(1950, len(year_population_change)):
            year_population += year_population_change[year]
            if year_population > max_population:
                max_population = year_population
                max_year = year
        return max_year
