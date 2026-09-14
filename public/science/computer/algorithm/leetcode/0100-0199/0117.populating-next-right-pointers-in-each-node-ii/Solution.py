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
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if root is None:
            return root
        q = deque([root])
        while q:
            p = None
            for _ in range(len(q)):
                node = q.popleft()
                if p:
                    p.next = node
                p = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root


# ----------------本地测试----------------
if __name__ == "__main__":
    # 完美二叉树
    #        1
    #      /   \
    #     2     3
    #    / \   / \
    #   4   5 6   7
    root = Node(1,
        Node(2, Node(4), Node(5)),
        Node(3, Node(6), Node(7))
    )
    Solution().connect(root)

    def print_level(node):
        res = []
        cur = node
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res

    print(print_level(root))          # [1]
    print(print_level(root.left))    # [2, 3]
    print(print_level(root.left.left))# [4,5,6,7]
