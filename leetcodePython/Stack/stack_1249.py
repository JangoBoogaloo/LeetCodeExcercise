class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        openBrackets = []
        for i in range(len(s)):
            if s[i] == '(':
                openBrackets.append(i)
            elif s[i] == ')':
                if len(openBrackets) > 0:
                    openBrackets.pop()
                else:
                    s[i] = ""
        for index in openBrackets:
            s[index] = ""
        return "".join(s)
