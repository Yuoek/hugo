import bisect

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = bisect.bisect_left(range(1, num + 1), num, key=lambda x: x * x) + 1
        return l * l == num

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPerfectSquare(16)) # True
    print(sol.isPerfectSquare(14)) # False
    print(sol.isPerfectSquare(1))  # True
    print(sol.isPerfectSquare(25)) # True
