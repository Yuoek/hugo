class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for c in map(ord, columnTitle):
            ans = ans * 26 + c - ord("A") + 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.titleToNumber("A"))
    print(sol.titleToNumber("AB"))
    print(sol.titleToNumber("ZY"))
