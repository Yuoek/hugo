class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n -= n & -n
            ans += 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.hammingWeight(0b00000000000000000000000000001011)) # 3
