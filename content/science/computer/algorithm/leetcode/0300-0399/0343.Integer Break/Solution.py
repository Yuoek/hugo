from typing import List

class Solution:
    def integerBreak(self, n: int) -> int:
        f = [1] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                f[i] = max(f[i], f[i - j] * j, (i - j) * j)
        return f[n]

if __name__ == "__main__":
    sol = Solution()
    print(sol.integerBreak(2))  # 1
    print(sol.integerBreak(10)) # 36
    print(sol.integerBreak(3))  # 2
    print(sol.integerBreak(8))  # 18
