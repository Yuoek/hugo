---
title: 0353.Design Snake Game
date: 2026-09-18
---

## Solution

```python
from collections import deque
from typing import List

class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.m = height
        self.n = width
        self.food = food
        self.score = 0
        self.idx = 0
        self.q = deque([(0, 0)])
        self.vis = {(0, 0)}

    def move(self, direction: str) -> int:
        i, j = self.q[0]
        x, y = i, j
        match direction:
            case "U":
                x -= 1
            case "D":
                x += 1
            case "L":
                y -= 1
            case "R":
                y += 1
        # 撞墙判定
        if x < 0 or x >= self.m or y < 0 or y >= self.n:
            return -1
        eat_food = False
        if self.idx < len(self.food) and x == self.food[self.idx][0] and y == self.food[self.idx][1]:
            self.score += 1
            self.idx += 1
            eat_food = True
        if not eat_food:
            self.vis.remove(self.q.pop())
        # 撞到自己身体
        if (x, y) in self.vis:
            return -1
        self.q.appendleft((x, y))
        self.vis.add((x, y))
        return self.score

# 本地测试
if __name__ == "__main__":
    # Example
    obj = SnakeGame(width=3, height=2, food=[[1,2],[0,1]])
    print(obj.move("R")) # 0
    print(obj.move("D")) # 0
    print(obj.move("R")) # 1
    print(obj.move("U")) # 1
    print(obj.move("L")) # 2
    print(obj.move("U")) # -1
```
