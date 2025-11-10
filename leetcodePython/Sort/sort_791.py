from functools import cmp_to_key


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        charList = list(s)
        def compare(a:str, b:str) -> int:
            aValue = order.index(a) if a in order else len(order)
            bValue = order.index(b) if b in order else len(order)
            return aValue - bValue
        charList.sort(key=cmp_to_key(compare))
        return "".join(charList)







