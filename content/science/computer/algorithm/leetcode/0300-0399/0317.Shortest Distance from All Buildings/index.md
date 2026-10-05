---
title: 0317 离建筑物最近的距离
date: 2026-09-10
---

## Solution

```python

from typing import List
from collections import deque
from math import inf

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        total = 0
        cnt = [[0] * n for _ in range(m)]
        dist = [[0] * n for _ in range(m)]
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total += 1
                    q = deque()
                    q.append((i, j))
                    d = 0
                    vis = set()
                    while q:
                        d += 1
                        for _ in range(len(q)):
                            r, c = q.popleft()
                            for a, b in dirs:
                                x, y = r + a, c + b
                                if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and (x, y) not in vis:
                                    cnt[x][y] += 1
                                    dist[x][y] += d
                                    vis.add((x, y))
                                    q.append((x, y))
        ans = inf
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and cnt[i][j] == total:
                    ans = min(ans, dist[i][j])
        return -1 if ans == inf else ans

def main():
    sol = Solution()
    print(sol.shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]))

if __name__ == "__main__":
    main()
```
