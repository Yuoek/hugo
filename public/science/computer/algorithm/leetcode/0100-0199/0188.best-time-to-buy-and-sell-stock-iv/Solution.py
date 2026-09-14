from typing import List
from functools import lru_cache

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dfs(i: int, j: int, hold: int) -> int:
            if i >= len(prices):
                return 0
            ans = dfs(i + 1, j, hold)
            if hold:
                ans = max(ans, prices[i] + dfs(i + 1, j, 0))
            elif j > 0:
                ans = max(ans, -prices[i] + dfs(i + 1, j - 1, 1))
            return ans
        return dfs(0, k, 0)

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit(2,[2,4,1]))
    print(sol.maxProfit(2,[3,2,6,5,0,3]))
