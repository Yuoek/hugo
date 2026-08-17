---
title: 0094 二叉树的中序遍历
date: 2026-08-17
weight: 94
summary: 二叉树
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)

        ans = []
        dfs(root)
        return ans

if __name__ == "__main__":
    # 构建 [1,null,2,3]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    sol = Solution()
    print(sol.inorderTraversal(root)) # [1,3,2]

```
