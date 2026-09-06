class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(t)
        f = [1] + [0] * n
        for a in s:
            for j in range(n, 0, -1):
                if a == t[j - 1]:
                    f[j] += f[j - 1]
        return f[n]


# ----------------本地测试----------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.numDistinct("rabbbit", "rabbit"))  # 3
    print(sol.numDistinct("babgbag", "bag"))     # 5
    print(sol.numDistinct("", ""))               # 1
    print(sol.numDistinct("a", ""))              # 1
    print(sol.numDistinct("", "a"))              # 0
