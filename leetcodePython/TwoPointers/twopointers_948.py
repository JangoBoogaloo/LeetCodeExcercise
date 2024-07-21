from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # strategy
        # if score 0, play token with smallest power to increase score
        # if score not 0, play token with biggest power to increase power

        tokens.sort()
        left, right = 0, len(tokens) - 1
        score = 0
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
            elif score > 0 and left < right:
                score -= 1
                power += tokens[right]
                right -= 1
            else:
                return score
        return score

