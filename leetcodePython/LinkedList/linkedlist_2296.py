class TextEditor:
    def __init__(self):
        self._cursorLeft = []
        self._cursorRight = []

    def addText(self, text: str) -> None:
        for ch in text:
            self._cursorLeft.append(ch)

    def deleteText(self, k: int) -> int:
        k = min(k, len(self._cursorLeft))
        for _ in range(k):
            self._cursorLeft.pop()
        return k

    def _getLeftChars(self, count: int = 10) -> str:
        txt = []
        for _ in range(count):
            if not self._cursorLeft:
                break
            txt.append(self._cursorLeft.pop())
        txt.reverse()
        for ch in txt:
            self._cursorLeft.append(ch)
        return "".join(txt)

    def cursorLeft(self, k: int) -> str:
        k = min(k, len(self._cursorLeft))

        for _ in range(k):
            ch = self._cursorLeft.pop()
            self._cursorRight.append(ch)
        return self._getLeftChars()

    def cursorRight(self, k: int) -> str:
        k = min(k, len(self._cursorRight))

        for _ in range(k):
            ch = self._cursorRight.pop()
            self._cursorLeft.append(ch)
        return self._getLeftChars()
