class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1
        if n % 3 == 0:
            return pow(3, n // 3)
        if n % 3 == 1:
            return pow(3, n // 3 - 1) * 4
        return pow(3, n // 3) * 2

if __name__ == "__main__":
    sol = Solution()
    print(sol.integerBreak(2))   # 1
    print(sol.integerBreak(3))   # 2
    print(sol.integerBreak(10))  # 36
    print(sol.integerBreak(8))   # 18
    print(sol.integerBreak(4))   # 4
