---
title: 0114 二叉树展开为链表
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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in‑place instead.
        """
        while root:
            if root.left:
                pre = root.left
                # 找到左子树最右下角节点
                while pre.right:
                    pre = pre.right
                # 把原来的右子树接到 pre.right
                pre.right = root.right
                # 左子树挪到右边
                root.right = root.left
                root.left = None
            root = root.right


# ----------------本地测试----------------
if __name__ == "__main__":
    #      1
    #    /   \
    #   2     5
    #  / \     \
    # 3   4     6
    root = TreeNode(1,
        TreeNode(2, TreeNode(3), TreeNode(4)),
        TreeNode(5, None, TreeNode(6))
    )
    Solution().flatten(root)

    # 遍历链表化之后的树
    p = root
    res = []
    while p:
        res.append(p.val)
        p = p.right
    print(res) # [1,2,3,4,5,6]
```
