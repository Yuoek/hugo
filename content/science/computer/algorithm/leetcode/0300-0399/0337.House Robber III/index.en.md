---
title: 0337.House Robber III
date: 2026-09-17
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
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> tuple[int, int]:
            if root is None:
                return 0, 0
            la, lb = dfs(root.left)
            ra, rb = dfs(root.right)
            # a: 选当前节点；b: 不选当前节点
            return root.val + lb + rb, max(la, lb) + max(ra, rb)

        return max(dfs(root))

if __name__ == "__main__":
    sol = Solution()
    # [3,2,3,null,3,null,1]
    n1 = TreeNode(3)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(3)
    n5 = TreeNode(1)
    n1.left, n1.right = n2, n3
    n2.right = n4
    n3.right = n5
    print(sol.rob(n1)) # 7
```
