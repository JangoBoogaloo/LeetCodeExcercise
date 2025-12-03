from typing import List
from union_find import UF
from string import ascii_lowercase

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UF()
        for ch in ascii_lowercase:
            uf.add(ch)

        for equation in equations:
            a, equal, _, b = equation
            if equal == "!" and a == b:
                return False
            if equal == "=":
                uf.union(a, b)

        for equation in equations:
            a, equal, _, b = equation
            if equal == "!" and uf.find(a) == uf.find(b):
                return False
        return True