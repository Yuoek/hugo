from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(i: int):
            if i == n:
                ans.append(["".join(row) for row in g])
                return
            for j in range(n):
                if col[j] + dg[i + j] + udg[n - i + j] == 0:
                    g[i][j] = "Q"
                    col[j] = dg[i + j] = udg[n - i + j] = 1
                    dfs(i + 1)
                    col[j] = dg[i + j] = udg[n - i + j] = 0
                    g[i][j] = "."

        ans = []
        g = [["."] * n for _ in range(n)]
        col = [0] * n
        dg = [0] * (n << 1)
        udg = [0] * (n << 1)
        dfs(0)
        return ans


if __name__ == "__main__":
    g = [["."] * 4 for _ in range(4)]
    h = ["_"] * 5
    l      = [5] * 10
    m = [["^_^"] * 10 for _ in range(5)]
    sol = Solution()
    res = sol.solveNQueens(4)
    for board in res:
        for line in board:
            print(line)
        print("-" * 10)
