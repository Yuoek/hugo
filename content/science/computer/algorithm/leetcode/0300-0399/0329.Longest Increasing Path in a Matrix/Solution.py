from typing import List
from functools import cache
from itertools import pairwise

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            ans = 0
            for a, b in pairwise((-1, 0, 1, 0, -1)):
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    ans = max(ans, dfs(x, y))
            return ans + 1

        m, n = len(matrix), len(matrix[0])
        return max(dfs(i, j) for i in range(m) for j in range(n))

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])) # 4
    print(sol.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]])) # 4
    print(sol.longestIncreasingPath([[1]])) # 1
