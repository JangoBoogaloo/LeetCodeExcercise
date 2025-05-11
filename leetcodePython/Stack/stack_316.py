class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        increaseCharStack = []
        seen = set()
        charLastIndex = {ch: i for i, ch in enumerate(s)}
        for i, ch in enumerate(s):
            if ch not in seen:
                while increaseCharStack and ch < increaseCharStack[-1] and i < charLastIndex[increaseCharStack[-1]]:
                    seen.discard(increaseCharStack.pop())
                seen.add(ch)
                increaseCharStack.append(ch)
        return "".join(increaseCharStack)




