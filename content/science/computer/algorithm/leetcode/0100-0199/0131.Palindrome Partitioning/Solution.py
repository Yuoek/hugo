from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(i: int):
            if i == n:
                ans.append(t[:])
                return
            for j in range(i, n):
                if f[i][j]:
                    t.append(s[i : j + 1])
                    dfs(j + 1)
                    t.pop()

        n = len(s)
        # f[i][j]：s[i..j] 是否为回文
        f = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = s[i] == s[j] and f[i + 1][j - 1]
        ans = []
        t = []
        dfs(0)
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.partition("aab"))
    # 输出：[["a","a","b"],["aa","b"]]
    print(sol.partition("a"))
    # 输出：[["a"]]
