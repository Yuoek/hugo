class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPerfectSquare(16)) # True
    print(sol.isPerfectSquare(14)) # False
    print(sol.isPerfectSquare(1))  # True
    print(sol.isPerfectSquare(25)) # True
