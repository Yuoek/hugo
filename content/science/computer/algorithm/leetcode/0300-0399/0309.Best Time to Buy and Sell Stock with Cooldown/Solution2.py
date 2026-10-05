from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        f = [[0] * 2 for _ in range(n)]
        f[0][1] = -prices[0]
        f[1][0] = max(0, f[0][1] + prices[1])
        f[1][1] = max(-prices[0], -prices[1])
        for i in range(2, n):
            f[i][0] = max(f[i - 1][0], f[i - 1][1] + prices[i])
            f[i][1] = max(f[i - 1][1], f[i - 2][0] - prices[i])
        return f[n - 1][0]


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([1,2,3,0,2])) # 3
    print(sol.maxProfit([1])) # 0
