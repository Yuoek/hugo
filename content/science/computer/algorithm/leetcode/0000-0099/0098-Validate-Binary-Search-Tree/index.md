---
title: 0098 验证二叉搜索树
date: 2026-08-17
weight: 98
summary: lc
---

## Solution

```python
from typing import Optional
from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]) -> bool:
            if root is None:
                return True
            if not dfs(root.left):
                return False
            nonlocal prev
            if prev >= root.val:
                return False
            prev = root.val
            return dfs(root.right)

        prev = -inf
        return dfs(root)

if __name__ == "__main__":
    sol = Solution()
    # [2,1,3]
    r1 = TreeNode(2, TreeNode(1), TreeNode(3))
    print(sol.isValidBST(r1)) # True
    # [5,1,4,null,null,3,6]
    r2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(sol.isValidBST(r2)) # False

```
