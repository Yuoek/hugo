from typing import List
from itertools import pairwise

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0, b - a) for a, b in pairwise(prices))


# ----------------本地测试----------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4])) # 7
    print(sol.maxProfit([1,2,3,4,5]))    # 4
    print(sol.maxProfit([7,6,4,3,1]))    # 0
