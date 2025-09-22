from typing import List


class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        maxDamage = max(damage)
        armorHelp = min(maxDamage, armor)
        return sum(damage) + 1 - armorHelp