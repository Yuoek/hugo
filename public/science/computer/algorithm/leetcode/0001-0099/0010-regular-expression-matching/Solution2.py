class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True

        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    f[i][j] = f[i][j - 2]
                    if i > 0 and (p[j - 2] == "." or s[i - 1] == p[j - 2]):
                        f[i][j] |= f[i - 1][j]
                else:
                    if i > 0 and (p[j - 1] == "." or s[i - 1] == p[j - 1]):
                        f[i][j] = f[i - 1][j - 1]
        return f[m][n]


# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.isMatch("aa", "a"))      # False
    print(sol.isMatch("aa", "a*"))     # True
    print(sol.isMatch("ab", ".*"))     # True
    print(sol.isMatch("aab", "c*a*b")) # True
    print(sol.isMatch("mississippi", "mis*is*p*.")) # False

