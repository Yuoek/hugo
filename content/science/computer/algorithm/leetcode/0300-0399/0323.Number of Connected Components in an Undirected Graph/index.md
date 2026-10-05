---
title: 0323 无向图中连通分量的数目
date: 2026-09-16
---

## Solution

```python
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(i: int) -> int:
            if i in vis:
                return 0
            vis.add(i)
            for j in g[i]:
                dfs(j)
            return 1

        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        vis = set()
        return sum(dfs(i) for i in range(n))

if __name__ == "__main__":
    sol = Solution()
    print(sol.countComponents(5, [[0,1],[1,2],[3,4]])) # 2
    print(sol.countComponents(5, [[0,1],[1,2],[2,3],[3,4]])) # 1

```

## Solution 2

```python
from typing import List

class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.size[pa] > self.size[pb]:
            self.p[pb] = pa
            self.size[pa] += self.size[pb]
        else:
            self.p[pa] = pb
            self.size[pb] += self.size[pa]
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for a, b in edges:
            n -= uf.union(a, b)
        return n

if __name__ == "__main__":
    sol = Solution()
    print(sol.countComponents(5, [[0,1],[1,2],[3,4]]))        # 2
    print(sol.countComponents(5, [[0,1],[1,2],[2,3],[3,4]]))  # 1
    print(sol.countComponents(4, []))                         # 4
```

## Solution 3

```python
from typing import List
from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        vis = set()
        ans = 0
        for i in range(n):
            if i in vis:
                continue
            vis.add(i)
            q = deque([i])
            while q:
                a = q.popleft()
                for b in g[a]:
                    if b not in vis:
                        vis.add(b)
                        q.append(b)
            ans += 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.countComponents(5, [[0,1],[1,2],[3,4]]))        # 2
    print(sol.countComponents(5, [[0,1],[1,2],[2,3],[3,4]]))  # 1
    print(sol.countComponents(4, []))                         # 4
```

