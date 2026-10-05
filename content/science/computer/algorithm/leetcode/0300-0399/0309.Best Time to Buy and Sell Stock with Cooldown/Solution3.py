from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        f, f0, f1 = 0, 0, -prices[0]
        for x in prices[1:]:
            f, f0, f1 = f0, max(f0, f1 + x), max(f1, f - x)
        return f0


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([1,2,3,0,2])) #3
    print(sol.maxProfit([1])) #0
