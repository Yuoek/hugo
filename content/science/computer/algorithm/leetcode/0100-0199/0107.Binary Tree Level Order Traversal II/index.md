---
title: 0107 二叉树的层序遍历 II
date: 2026-09-03
---

## Solution

```python
from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        q = deque([root])
        while q:
            t = []
            for _ in range(len(q)):
                node = q.popleft()
                t.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(t)
        return ans[::-1]


# ----------------本地测试----------------
if __name__ == "__main__":
    #      3
    #    /   \
    #   9    20
    #       /  \
    #      15   7
    root = TreeNode(3,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7))
    )
    print(Solution().levelOrderBottom(root))
    # [[15, 7], [9, 20], [3]]

    print(Solution().levelOrderBottom(None)) # []
    print(Solution().levelOrderBottom(TreeNode(1))) # [[1]]
```
