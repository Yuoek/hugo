---
title: 0124.Binary Tree Maximum Path Sum
date: 2026-09-03
---

## Solution

```python
from typing import Optional
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            nonlocal ans
            ans = max(ans, root.val + left + right)
            return root.val + max(left, right)

        ans = -math.inf
        dfs(root)
        return ans


# ----------------本地测试----------------
if __name__ == "__main__":
    sol = Solution()
    # [-10,9,20,null,null,15,7]
    root1 = TreeNode(-10,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7))
    )
    print(sol.maxPathSum(root1)) # 42

    # 全部负数树 [‑3]
    root2 = TreeNode(-3)
    print(sol.maxPathSum(root2)) # -3
```
