from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        d = {}
        dummy = tail = Node(0)
        cur = head
        # 第一遍：复制所有节点，构建next关系，建立映射
        while cur:
            node = Node(cur.val)
            tail.next = node
            tail = tail.next
            d[cur] = node
            cur = cur.next
        # 第二遍：填充random指针
        cur = head
        while cur:
            d[cur].random = d[cur.random] if cur.random else None
            cur = cur.next
        return dummy.next


# 本地测试
if __name__ == "__main__":
    # 构造链表
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
    copy = sol.copyRandomList(n1)
    p = copy
    while p:
        print(p.val, p.random.val if p.random else None)
        p = p.next
