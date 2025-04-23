class Node:
    def __init__(self, url: str):
        self.url = url
        self.next = None
        self.prev = None


class BrowserHistory:
    def __init__(self, homepage: str):
        self.current = Node(homepage)

    def visit(self, url: str) -> None:
        self.current.next = Node(url)
        self.current.next.prev = self.current
        self.current = self.current.next

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.current.prev is None:
                break
            self.current = self.current.prev
        return self.current.url

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.current.next is None:
                break
            self.current = self.current.next
        return self.current.url
