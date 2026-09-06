---
 title: 0191 位 1 的个数
 date: 2026-09-06
---

## Solution

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n &= n - 1
            ans += 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.hammingWeight(0b00000000000000000000000000001011)) #3
```

## Solution 2

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n -= n & -n
            ans += 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.hammingWeight(0b00000000000000000000000000001011)) # 3
```
