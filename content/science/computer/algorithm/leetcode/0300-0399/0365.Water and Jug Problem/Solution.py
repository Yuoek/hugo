from typing import Set

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        def dfs(i: int, j: int) -> bool:
            if (i, j) in vis:
                return False
            vis.add((i, j))
            if i == z or j == z or i + j == z:
                return True
            # 装满x / 装满y / 倒空x / 倒空y
            if dfs(x, j) or dfs(i, y) or dfs(0, j) or dfs(i, 0):
                return True
            # x -> y 倒水，y -> x倒水
            a = min(i, y - j)
            b = min(j, x - i)
            return dfs(i - a, j + a) or dfs(i + b, j - b)

        vis = set()
        return dfs(0, 0)

# 本地测试
if __name__ == "__main__":
    sol = Solution()
    print(sol.canMeasureWater(3,5,4)) # True
    print(sol.canMeasureWater(2,6,5)) # False
    print(sol.canMeasureWater(1,2,3)) # True
