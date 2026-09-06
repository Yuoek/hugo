---
title: 0106.Construct Binary Tree from Inorder and Postorder Traversal
date: 2026-09-03
---

## Solution

```python
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def dfs(i: int, j: int, n: int) -> Optional[TreeNode]:
            if n <= 0:
                return None
            v = postorder[j + n - 1]
            k = d[v]
            l = dfs(i, j, k - i)
            r = dfs(k + 1, j + (k - i), n - (k - i) - 1)
            return TreeNode(v, l, r)

        d = {v: idx for idx, v in enumerate(inorder)}
        return dfs(0, 0, len(inorder))


# ----------------本地测试----------------
if __name__ == "__main__":
    #      3
    #    /   \
    #   9    20
    #       /  \
    #      15   7
    ino  = [9,3,15,20,7]
    post = [9,15,7,20,3]

    root = Solution().buildTree(ino, post)

    # 前序遍历校验
    def pre_show(node):
        if not node:
            return []
        return [node.val] + pre_show(node.left) + pre_show(node.right)

    print(pre_show(root)) # [3, 9, 20, 15, 7]

    print(Solution().buildTree([], [])) # None
    print(pre_show(Solution().buildTree([1], [1]))) # [1]
```
