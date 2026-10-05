---
title: 0333 最大二叉搜索子树
date: 2026-09-17
---

## Solution

```python
from typing import Optional
from math import inf

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root is None:
                return inf, -inf, 0
            lmi, lmx, ln = dfs(root.left)
            rmi, rmx, rn = dfs(root.right)
            nonlocal ans
            if lmx < root.val < rmi:
                ans = max(ans, ln + rn + 1)
                return min(lmi, root.val), max(rmx, root.val), ln + rn + 1
            return -inf, inf, 0

        ans = 0
        dfs(root)
        return ans

if __name__ == "__main__":
    # 构造样例 [10,5,15,1,8,null,7]
    n1 = TreeNode(10)
    n2 = TreeNode(5)
    n3 = TreeNode(15)
    n4 = TreeNode(1)
    n5 = TreeNode(8)
    n6 = TreeNode(7)
    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5
    n3.right = n6
    sol = Solution()
    print(sol.largestBSTSubtree(n1)) # 3
```
