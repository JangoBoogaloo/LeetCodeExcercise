from collections import deque
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deckIndex = deque([i for i in range(len(deck))])
        deck.sort()
        newOrder = [0] * len(deck)
        for card in deck:
            index = deckIndex.popleft()
            newOrder[index] = card
            if deckIndex:
                deckIndex.append(deckIndex.popleft())
        return newOrder






