import math


class Solution:
    def calculate(self, s: str) -> int:
        nums = []
        curr_num = 0
        pre_op = '+'
        s += '+'
        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + ord(ch) - ord('0')
            elif ch.isspace():
                pass
            else:
                if pre_op == '+':
                    nums.append(curr_num)
                elif pre_op == '-':
                    nums.append(-curr_num)
                elif pre_op == '*':
                    nums.append(nums.pop() * curr_num)
                elif pre_op == '/':
                    nums.append(math.trunc(nums.pop()/curr_num))
                curr_num = 0
                pre_op = ch
        return sum(nums)