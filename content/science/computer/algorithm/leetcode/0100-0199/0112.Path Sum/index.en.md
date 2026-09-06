---
title: 0112.Path Sum
date: 2026-09-03
---

```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, s):
            if root is None:
                return False
            s += root.val
            # 必须是叶子节点，并且累加和等于目标
            if root.left is None and root.right is None and s == targetSum:
                return True
            return dfs(root.left, s) or dfs(root.right, s)

        return dfs(root, 0)


# ----------------本地测试----------------
if __name__ == "__main__":
    #       5
    #     /   \
    #    4     8
    #   /     / \
    #  11    13  4
    # /  \        \
    #7    2        1
    root1 = TreeNode(5,
        TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
        TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))
    )
    print(Solution().hasPathSum(root1, 22)) # True  5‑4‑11‑2 =22
    print(Solution().hasPathSum(root1, 100)) # False

    root2 = TreeNode(1, TreeNode(2))
    print(Solution().hasPathSum(root2, 1)) # False，1不是叶子

    print(Solution().hasPathSum(None, 0)) # False
    print(Solution().hasPathSum(TreeNode(3), 3)) # True
```
