from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        def inorder(root):
            if root:
                inorder(root.left)
                self.vals.append(root.val)
                inorder(root.right)

        self.cur = 0
        self.vals = []
        inorder(root)

    def next(self) -> int:
        res = self.vals[self.cur]
        self.cur += 1
        return res

    def hasNext(self) -> bool:
        return self.cur < len(self.vals)

if __name__ == "__main__":
    # 建树 [7,3,15,null,null,9,20]
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)
    it = BSTIterator(root)
    print(it.next())
    print(it.next())
    print(it.hasNext())
    print(it.next())
