---
title: 0111 二叉树的最小深度
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        # 左为空：只能看右子树
        if root.left is None:
            return 1 + self.minDepth(root.right)
        # 右为空：只能看左子树
        if root.right is None:
            return 1 + self.minDepth(root.left)
        # 左右都存在，取较小
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


# ----------------本地测试----------------
if __name__ == "__main__":
    #     3
    #    / \
    #   9  20
    #      / \
    #     15  7
    root1 = TreeNode(3,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7))
    )
    print(Solution().minDepth(root1)) # 2

    # 单边树：1->2->3，叶子在最底下
    #    1
    #     \
    #      2
    #       \
    #        3
    root2 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    print(Solution().minDepth(root2)) # 3

    print(Solution().minDepth(None)) # 0
    print(Solution().minDepth(TreeNode(5))) # 1
```

## Solution 2

```python
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = deque([root])
        ans = 0
        while True:
            ans += 1
            for _ in range(len(q)):
                node = q.popleft()
                # 遇到第一个叶子节点，直接返回当前层数
                if node.left is None and node.right is None:
                    return ans
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)


# ----------------本地测试----------------
if __name__ == "__main__":
    #      3
    #    /   \
    #   9    20
    #       /  \
    #      15   7
    root1 = TreeNode(3,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7))
    )
    print(Solution().minDepth(root1)) # 2

    # 单边树
    #    1
    #     \
    #      2
    #       \
    #        3
    root2 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    print(Solution().minDepth(root2)) # 3

    print(Solution().minDepth(None)) # 0
    print(Solution().minDepth(TreeNode(5))) # 1

```
