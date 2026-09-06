---
title: 0102.Binary Tree Level Order Traversal
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        q = deque([root])
        while q:
            t = []
            # len(q)：这一层节点的数量，进入循环瞬间固定
            for _ in range(len(q)):
                node = q.popleft()
                t.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(t)
        return ans


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
    print(Solution().levelOrder(root))
    # [[3], [9, 20], [15, 7]]

    # 空树
    print(Solution().levelOrder(None)) # []

    # 单节点
    print(Solution().levelOrder(TreeNode(1))) # [[1]]
```
