---
title: 0150 逆波兰表达式求值
date: 2026-09-05
---

## Solution

```python
from typing import List
import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opt = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }
        s = []
        for token in tokens:
            if token in opt:
                s.append(int(opt[token](s.pop(-2), s.pop(-1))))
            else:
                s.append(int(token))
        return s[0]

if __name__ == "__main__":
    sol = Solution()
    print(sol.evalRPN(["2","1","+","3","*"]))
    print(sol.evalRPN(["4","13","5","/","+"]))
```

## Solution 2

```python
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for t in tokens:
            if len(t) > 1 or t.isdigit():
                nums.append(int(t))
            else:
                if t == "+":
                    nums[-2] += nums[-1]
                elif t == "-":
                    nums[-2] -= nums[-1]
                elif t == "*":
                    nums[-2] *= nums[-1]
                else:
                    nums[-2] = int(nums[-2] / nums[-1])
                nums.pop()
        return nums[0]

if __name__ == "__main__":
    sol = Solution()
    print(sol.evalRPN(["2","1","+","3","*"]))
    print(sol.evalRPN(["4","13","5","/","+"]))
    print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
```
