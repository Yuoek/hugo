---
title: 0101 对称二叉树
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            if root1 == root2:
                return True
            if root1 is None or root2 is None or root1.val != root2.val:
                return False
            return dfs(root1.left, root2.right) and dfs(root1.right, root2.left)

        return dfs(root.left, root.right)


# ---------------------- 本地测试 ----------------------
if __name__ == "__main__":
    # 测试1 镜像对称
    root1 = TreeNode(1,
        TreeNode(2, TreeNode(3), TreeNode(4)),
        TreeNode(2, TreeNode(4), TreeNode(3))
    )
    print(Solution().isSymmetric(root1))  # True

    # 测试2 不对称
    root2 = TreeNode(1,
        TreeNode(2, None, TreeNode(3)),
        TreeNode(2, None, TreeNode(3))
    )
    print(Solution().isSymmetric(root2))  # False

    # 测试3 只有根节点
    root3 = TreeNode(10)
    print(Solution().isSymmetric(root3))  # True

    # 测试4 空树
    root4 = None
    print(Solution().isSymmetric(root4))  # True
```
