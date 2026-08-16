class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l < r:
            mid = (l + r + 1) >> 1
            if mid > x // mid:
                r = mid - 1
            else:
                l = mid
        return l

if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(4))   # 2
    print(sol.mySqrt(8))   # 2
    print(sol.mySqrt(0))   # 0
    print(sol.mySqrt(1))   # 1
    print(sol.mySqrt(2147395599))
