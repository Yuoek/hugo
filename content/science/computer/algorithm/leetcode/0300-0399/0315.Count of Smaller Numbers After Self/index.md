---
title: 0315.Count of Smaller Numbers After Self
date: 2026-09-10
---

## Solution

```python
from typing import List

class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.c = [0] * (n + 1)

    @staticmethod
    def lowbit(x):
        return x & -x

    def update(self, x, delta):
        while x <= self.n:
            self.c[x] += delta
            x += BinaryIndexedTree.lowbit(x)

    def query(self, x):
        s = 0
        while x > 0:
            s += self.c[x]
            x -= BinaryIndexedTree.lowbit(x)
        return s


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        alls = sorted(set(nums))
        m = {v: i for i, v in enumerate(alls, 1)}
        tree = BinaryIndexedTree(len(m))
        ans = []
        for v in nums[::-1]:
            x = m[v]
            tree.update(x, 1)
            ans.append(tree.query(x - 1))
        return ans[::-1]

def main():
    sol = Solution()
    print(sol.countSmaller([5,2,6,1])) # [2,1,1,0]

if __name__ == "__main__":
    main()
```

## Solution 2

```python
from typing import List

class Node:
    def __init__(self):
        self.l = 0
        self.r = 0
        self.v = 0


class SegmentTree:
    def __init__(self, n):
        self.tr = [Node() for _ in range(n << 2)]
        self.build(1, 1, n)

    def build(self, u, l, r):
        self.tr[u].l = l
        self.tr[u].r = r
        if l == r:
            return
        mid = (l + r) >> 1
        self.build(u << 1, l, mid)
        self.build(u << 1 | 1, mid + 1, r)

    def modify(self, u, x, v):
        if self.tr[u].l == x and self.tr[u].r == x:
            self.tr[u].v += v
            return
        mid = (self.tr[u].l + self.tr[u].r) >> 1
        if x <= mid:
            self.modify(u << 1, x, v)
        else:
            self.modify(u << 1 | 1, x, v)
        self.pushup(u)

    def query(self, u, l, r):
        if self.tr[u].l >= l and self.tr[u].r <= r:
            return self.tr[u].v
        mid = (self.tr[u].l + self.tr[u].r) >> 1
        v = 0
        if l <= mid:
            v += self.query(u << 1, l, r)
        if r > mid:
            v += self.query(u << 1 | 1, l, r)
        return v

    def pushup(self, u):
        self.tr[u].v = self.tr[u << 1].v + self.tr[u << 1 | 1].v


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        s = sorted(set(nums))
        m = {v: i for i, v in enumerate(s, 1)}
        tree = SegmentTree(len(s))
        ans = []
        for v in nums[::-1]:
            x = m[v]
            ans.append(tree.query(1, 1, x - 1))
            tree.modify(1, x, 1)
        return ans[::-1]

def main():
    sol = Solution()
    print(sol.countSmaller([5,2,6,1]))

if __name__ == "__main__":
    main()

```

## Solution 3

```python
from typing import List

class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        self.right_smaller_counts = [0] * len(nums]

        nums_indices = [(num, idx) for idx, num in enumerate(nums)]
        self.merge_sort(nums_indices)

        return self.right_smaller_counts

    def combine_arrays(
        self,
        left_nums_indices: list[tuple[int, int]],
        right_nums_indices: list[tuple[int, int]],
    ) -> list[tuple[int, int]]:
        merged_nums_indices: list[tuple[int, int]] = []
        left_idx, right_idx = 0, 0

        while left_idx < len(left_nums_indices) and right_idx < len(right_nums_indices):
            if left_nums_indices[left_idx][0] <= right_nums_indices[right_idx][0]:
                left_num_idx = left_nums_indices[left_idx][1]
                self.right_smaller_counts[left_num_idx] += right_idx

                merged_nums_indices.append(left_nums_indices[left_idx])
                left_idx += 1
                continue

            merged_nums_indices.append(right_nums_indices[right_idx])
            right_idx += 1

        while left_idx < len(left_nums_indices):
            left_num_idx = left_nums_indices[left_idx][1]
            self.right_smaller_counts[left_num_idx] += len(right_nums_indices)

            merged_nums_indices.append(left_nums_indices[left_idx])
            left_idx += 1

        while right_idx < len(right_nums_indices):
            merged_nums_indices.append(right_nums_indices[right_idx])
            right_idx += 1

        return merged_nums_indices

    def merge_sort(self, nums_indices: list[tuple[int, int]]) -> list[tuple[int, int]]:
        if len(nums_indices) == 1:
            return nums_indices

        split_idx = len(nums_indices) // 2

        left_nums_indices = self.merge_sort(nums_indices[:split_idx])
        right_nums_indices = self.merge_sort(nums_indices[split_idx:])

        return self.combine_arrays(left_nums_indices, right_nums_indices)

def main():
    sol = Solution()
    print(sol.countSmaller([5,2,6,1]))

if __name__ == "__main__":
    main()

```
