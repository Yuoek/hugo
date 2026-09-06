---
title: 0110.Balanced Binary Tree
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            l, r = height(root.left), height(root.right)
            # -1 代表子树已经不平衡，向上传递失败标记
            if l == -1 or r == -1 or abs(l - r) > 1:
                return -1
            return 1 + max(l, r)

        return height(root) >= 0


# ----------------本地测试----------------
if __name__ == "__main__":
    # 平衡树
    #      3
    #    /   \
    #   9    20
    #       /  \
    #      15   7
    root1 = TreeNode(3,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7))
    )
    print(Solution().isBalanced(root1)) # True

    # 不平衡：单边很深
    #       1
    #      /
    #     2
    #    /
    #   3
    root2 = TreeNode(1, TreeNode(2, TreeNode(3)), None)
    print(Solution().isBalanced(root2)) # False

    print(Solution().isBalanced(None)) # True
    print(Solution().isBalanced(TreeNode(5))) # True
```
