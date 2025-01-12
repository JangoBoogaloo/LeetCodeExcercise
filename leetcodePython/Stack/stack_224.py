class Solution:
    def calculate(self, s: str) -> int:
        curr_num = 0
        ans = 0
        sign = 1
        stack = []
        # 2-(3+4)
        s += '+'
        for ch in s:
            if ch.isdigit():
                curr_num = 10*curr_num + int(ch)
            elif ch in '-+':
                # 0+2 = 2
                # 0+3 = 3
                ans = ans + sign * curr_num
                sign = -1 if ch == '-' else 1
                curr_num = 0
            elif ch == '(':
                # 2
                stack.append(ans)
                # -1
                stack.append(sign)
                ans = 0
                sign = 1
            elif ch == ')':
                # 3 + 1*4 = 7
                ans = ans + sign * curr_num
                # -1
                exp_sign = stack.pop()
                # 2
                prev_ans = stack.pop()
                # 2 + -1*7
                ans = prev_ans + exp_sign * ans
                curr_num = 0
        return ans
