---
tile: 0310 最小高度树
date: 2026-09-09
---

## Solution

```python
from typing import List
from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        g = [[] for _ in range(n)]
        degree = [0] * n
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
            degree[a] += 1
            degree[b] += 1
        q = deque(i for i in range(n) if degree[i] == 1)
        ans = []
        while q:
            ans.clear()
            for _ in range(len(q)):
                a = q.popleft()
                ans.append(a)
                for b in g[a]:
                    degree[b] -= 1
                    if degree[b] == 1:
                        q.append(b)
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMinHeightTrees(4, [[1,0],[1,2],[1,3]])) # [1]
    print(sol.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])) # [3,4]
```
