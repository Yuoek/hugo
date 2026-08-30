---
title: 0095 不同的二叉搜索树 II
date: 2026-08-17
weight: 95
summary: 区间DFS
---

## Solution

```python
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(i: int, j: int) -> List[Optional[TreeNode]]:
            if i > j:
                return [None]
            ans = []
            for v in range(i, j + 1):
                left = dfs(i, v - 1)
                right = dfs(v + 1, j)
                for l in left:
                    for r in right:
                        ans.append(TreeNode(v, l, r))
            return ans
        if n == 0:
            return []
        return dfs(1, n)

# 测试输出辅助（前序打印）
def pre(root):
    res = []
    def d(x):
        if not x: return
        res.append(x.val)
        d(x.left)
        d(x.right)
    d(root)
    return res

if __name__ == "__main__":
    sol = Solution()
    for t in sol.generateTrees(3):
        print(pre(t))

```
