from typing import List
from functools import lru_cache

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @lru_cache(maxsize=None)
        def dfs(i: int, j: int) -> int:
            if i >= m or j >= n or obstacleGrid[i][j]:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            return dfs(i + 1, j) + dfs(i, j + 1)

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        return dfs(0, 0)

if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])) # 2
    print(sol.uniquePathsWithObstacles([[0,1]]))                   # 0
    print(sol.uniquePathsWithObstacles([[1,0]]))                   # 0
