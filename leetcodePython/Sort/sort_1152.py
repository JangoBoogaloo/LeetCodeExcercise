import collections
from itertools import combinations
from typing import List


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_sorted_site = collections.defaultdict(list)
        sorted_user_time_site = sorted(zip(username, timestamp, website), key= lambda x: (x[0], x[1]))
        for user, time, site in sorted_user_time_site:
            user_sorted_site[user].append(site)

        pattern_freq = collections.Counter()
        for user, sites in user_sorted_site.items():
            # from all the site visit take 3 site sub-sequent to build pattern combination
            # since site might be same which cause duplicate, use set to avoid, a singler user visit a pattern many times does not count as score
            user_pattern = set(combinations(sites, 3))

            # add the score for patterns for this user
            pattern_freq.update(user_pattern)
        lexico_pattern_freq = sorted(pattern_freq)
        return max(lexico_pattern_freq, key=pattern_freq.get)

