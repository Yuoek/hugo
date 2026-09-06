---
title: 0104 二叉树的最大深度
date: 2026-09-03
---

## Solution

```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        l, r = self.maxDepth(root.left), self.maxDepth(root.right)
        return 1 + max(l, r)


# ----------------本地测试----------------
if __name__ == "__main__":
    #      3
    #    /   \
    #   9    20
    #       /  \
    #      15   7
    root1 = TreeNode(3,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7))
    )
    print(Solution().maxDepth(root1)) # 3

    root2 = TreeNode(1, None, TreeNode(2))
    print(Solution().maxDepth(root2)) # 2

    root3 = None
    print(Solution().maxDepth(root3)) # 0

    root4 = TreeNode(5)
    print(Solution().maxDepth(root4)) # 1
```
