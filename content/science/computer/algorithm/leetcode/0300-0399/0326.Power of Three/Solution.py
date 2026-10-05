class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 2:
            if n % 3:
                return False
            n //= 3
        return n == 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPowerOfThree(27))   # True
    print(sol.isPowerOfThree(0))    # False
    print(sol.isPowerOfThree(9))    # True
    print(sol.isPowerOfThree(45))   # False
    print(sol.isPowerOfThree(1))    # True
