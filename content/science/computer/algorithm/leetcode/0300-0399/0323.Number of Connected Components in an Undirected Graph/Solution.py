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
