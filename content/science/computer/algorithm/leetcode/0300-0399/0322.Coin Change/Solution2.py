from typing import List
from math import inf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount
        f = [0] + [inf] * n
        for x in coins:
            for j in range(x, n + 1):
                f[j] = min(f[j], f[j - x] + 1)
        return -1 if f[n] >= inf else f[n]

if __name__ == "__main__":
    sol = Solution()
    print(sol.coinChange([1,2,5], 11)) # 3
    print(sol.coinChange([2], 3))      # -1
    print(sol.coinChange([1], 0))      # 0
