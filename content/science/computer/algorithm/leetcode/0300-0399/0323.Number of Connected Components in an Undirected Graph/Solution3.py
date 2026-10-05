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
