import collections
from typing import List


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self._directions = {
            "L": (-1, 0),
            "R": (1, 0),
            "U": (0, -1),
            "D": (0, 1)
        }
        self._width, self._height = width, height
        self._food = food
        self._food_index = 0
        initial = (0, 0)
        self._snake = collections.deque()
        self._snake.append(initial)
        self._used = set()
        self._used.add(initial)
        self._score = 0

    def _pos_valid(self, pos: tuple[int, int]) -> bool:
        x, y = pos
        if x < 0 or x >= self._width:
            return False
        if y < 0 or y >= self._height:
            return False
        if pos in self._used:
            return False
        return True

    def move(self, direction: str) -> int:
        x, y = self._directions[direction]
        head_x, head_y = self._snake[-1]
        new_head = (head_x + x, head_y + y)
        tail = self._snake[0]
        if new_head != tail and not self._pos_valid(new_head):
            return -1
        if self._food_index < len(self._food) and new_head[0] == self._food[self._food_index][1] and new_head[1] == self._food[self._food_index][0]:
            self._score += 1
            self._food_index += 1
        else:
            self._snake.popleft()
            self._used.remove(tail)
        self._used.add(new_head)
        self._snake.append(new_head)
        return self._score
