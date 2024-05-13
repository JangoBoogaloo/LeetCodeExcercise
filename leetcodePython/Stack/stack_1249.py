class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove = []
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    remove.append(i)
        # since we save the index and want to remove char, we ended up reverse remove
        for open_index in reversed(stack):
            s = s[:open_index] + s[open_index+1:]
        for index in reversed(remove):
            s = s[:index] + s[index+1:]
        return s