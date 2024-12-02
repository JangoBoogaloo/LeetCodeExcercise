class MyQueue:

    def __init__(self):
        self._stack_input = []
        self._stack_output = []

    def push(self, x: int) -> None:
        self._stack_input.append(x)

    def pop(self) -> int:
        self.peek()
        return self._stack_output.pop()

    def peek(self) -> int:
        if not self._stack_output:
            while self._stack_input:
                self._stack_output.append(self._stack_input.pop())
        return self._stack_output[-1]

    def empty(self) -> bool:
        return not self._stack_input and not self._stack_output
