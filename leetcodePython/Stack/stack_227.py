import math


class Solution:
    def calculate(self, s: str) -> int:
        ops = {"*", "/", "+", "-"}
        nums = []
        num = 0
        s += "+"
        prevOps = "+"
        for ch in s:
            if ch.isspace():
                continue
            if ch.isdigit():
                num = num * 10 + int(ch)
                continue
            if ch in ops:
                if prevOps == "+":
                    nums.append(num)
                elif prevOps == "-":
                    nums.append(-num)
                elif prevOps == "*":
                    nums.append(nums.pop() * num)
                else:
                    nums.append(math.trunc(nums.pop() / num))
                num = 0
                prevOps = ch
        return sum(nums)
