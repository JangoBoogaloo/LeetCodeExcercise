from typing import List


class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        max_damage = max(damage)
        armor = min(max_damage, armor)
        found = False
        health = 1
        for dmg in damage:
            if dmg == max_damage and not found:
                dmg -= armor
                found = True
            health += dmg
        return health