from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return None
        cur = head
        # 第一步：复制节点，插在原节点后面
        while cur:
            node = Node(cur.val, cur.next)
            cur.next = node
            cur = node.next
        
        # 第二步：赋值random指针
        cur = head
        while cur:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next
        
        # 第三步：拆分原链表与克隆链表
        cur = head
        ans = head.next
        while cur.next:
            node = cur.next
            cur.next = node.next
            cur = node
        return ans


# 测试用例
if __name__ == "__main__":
    n1 = Node(7)
    n2 = Node(13)
    n3 = Node(11)
    n4 = Node(10)
    n5 = Node(1)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n1.random = None
    n2.random = n1
    n3.random = n5
    n4.random = n3
    n5.random = n1

    sol = Solution()
    res = sol.copyRandomList(n1)
    p = res
    while p:
        print(p.val, p.random.val if p.random else None)
        p = p.next
