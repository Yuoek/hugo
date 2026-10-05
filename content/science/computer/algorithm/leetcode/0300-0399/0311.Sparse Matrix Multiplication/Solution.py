from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, n = len(mat1), len(mat2[0])
        p = len(mat2)
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for k in range(p):
                    ans[i][j] += mat1[i][k] * mat2[k][j]
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.multiply([[1,2],[3,4]], [[5,6],[7,8]]))
    # [[19,22],[43,50]]
