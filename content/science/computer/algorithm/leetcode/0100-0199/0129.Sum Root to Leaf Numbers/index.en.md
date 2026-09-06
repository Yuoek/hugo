---
title: 0129.Sum Root to Leaf Numbers
date: 2026-09-04
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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, s):
            if root is None:
                return 0
            s = s * 10 + root.val
            if root.left is None and root.right is None:
                return s
            return dfs(root.left, s) + dfs(root.right, s)

        return dfs(root, 0)

# 测试用例
if __name__ == "__main__":
    # 树: 1
    #    / \
    #   2   3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    sol = Solution()
    print(sol.sumNumbers(root)) # 12 + 13 = 25

    # 树: 4
    #    / \
    #   9   0
    #  / \
    # 5   1
    root2 = TreeNode(4)
    root2.left = TreeNode(9)
    root2.right = TreeNode(0)
    root2.left.left = TreeNode(5)
    root2.left.right = TreeNode(1)
    print(sol.sumNumbers(root2)) # 495 + 491 + 40 = 1026
```
