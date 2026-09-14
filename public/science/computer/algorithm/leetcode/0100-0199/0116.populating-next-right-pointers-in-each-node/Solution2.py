from collections import deque
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(left, right):
            if left is None or right is None:
                return
            left.next = right
            dfs(left.left, left.right)
            dfs(left.right, right.left)
            dfs(right.left, right.right)

        if root:
            dfs(root.left, root.right)
        return root

# ----------------本地测试----------------
if __name__ == "__main__":
    # 构建树
    #        1
    #      /   \
    #     2     3
    #    / \     \
    #   4   5     7
    root = Node(1,
        Node(2, Node(4), Node(5)),
        Node(3, None, Node(7))
    )
    Solution().connect(root)

    # 层序打印next指针
    def print_next(node):
        res = []
        cur = node
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res

    print(print_next(root))          # [1]
    print(print_next(root.left))    # [2,3]
    print(print_next(root.left.left))# [4,5,7]
