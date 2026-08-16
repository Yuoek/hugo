class Solution:
    def myPow(self, x: float, n: int) -> float:
        def qpow(a: float, n: int) -> float:
            ans = 1
            while n:
                if n & 1:
                    ans *= a
                a *= a
                n >>= 1
            return ans

        return qpow(x, n) if n >= 0 else 1 / qpow(x, -n)

if __name__ == "__main__":
    sol = Solution()
    print(sol.myPow(2.00000, 10))   # 1024.0
    print(sol.myPow(2.10000, 3))    # 9.261
    print(sol.myPow(2.00000, -2))   # 0.25
