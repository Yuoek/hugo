---
title: 0006_Z字形变换
weight: 6
---

## Solution

```python
from itertools import chain

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        g = [[] for _ in range(numRows)]
        i, k = 0, -1
        for c in s:
            g[i].append(c)
            if i == 0 or i == numRows - 1:
                k = -k
            i += k
        return ''.join(chain(*g))


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("PAYPALISHIRING", 3),
        ("PAYPALISHIRING", 4),
        ("A", 1),
        ("AB", 1),
        ("ABCDE", 2)
    ]
    for s, rows in test_cases:
        res = sol.convert(s, rows)
        print(f"s={repr(s)}, rows={rows} → {repr(res)}")

```

{{< reveal height="36em" >}}

<section data-transition="convex" data-transition-speed="fast">
<h2>Dear Sophie</h2>
 <section data-markdown>
  <textarea data-template>
    ## Slide 1
    A paragraph with some text and a [link](https://hakim.se).
    ---
    ## Slide 2
    $\alpha$
    ---
    ## Slide 3
    ```python
from itertools import chain

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        g = [[] for _ in range(numRows)]
        i, k = 0, -1
        for c in s:
            g[i].append(c)
            if i == 0 or i == numRows - 1:
                k = -k
            i += k
        return ''.join(chain(*g))


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("PAYPALISHIRING", 3),
        ("PAYPALISHIRING", 4),
        ("A", 1),
        ("AB", 1),
        ("ABCDE", 2)
    ]
    for s, rows in test_cases:
        res = sol.convert(s, rows)
        print(f"s={repr(s)}, rows={rows} → {repr(res)}")
    
    ```
  </textarea>
</section>
</section>
<!-- 这一页使用zoom缩放转场 -->
<section data-transition="none">
  <h2>这一页缩放切换</h2>
</section>
<section data-transition="none">
  <h2>这二页缩放切换</h2>
</section>
<section data-transition="zoom">
  <h2>这二页缩放切换</h2>
</section>

<!-- 单页指定速度 -->
<section>
<h2>Revealjs</h2>
<p>Yuoek： 你好虞</p>
</section>

 <section>
  <h2>The Lorenz Equations</h2>
$$
\begin{aligned}
\dot{x} & = \sigma(y-x) \\
\dot{y} & = \rho x - y - xz \\
\dot{z} & = -\beta z + xy
\end{aligned}
$$
</section>

<section data-auto-animate>
<pre data-id="code-animation"><code class="hljs python" data-trim data-line-numbers>
import { useState } from 'react';
# 导入库
from itertools import chain

# 定义类
class Solution:

# 程序入口
if __name__ == "__main__":
</code></pre>
<p> Leetcode 0006 Solution</p>
</section>

<section data-auto-animate>
<pre
data-id="code-animation"
><code class="hljs python" data-trim data-line-numbers="|4,8-11|17|22-24|28">
from itertools import chain

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        g = [[] for _ in range(numRows)]
        i, k = 0, -1
        for c in s:
            g[i].append(c)
            if i == 0 or i == numRows - 1:
                k = -k
            i += k
        return ''.join(chain(*g))


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("PAYPALISHIRING", 3),
        ("PAYPALISHIRING", 4),
        ("A", 1),
        ("AB", 1),
        ("ABCDE", 2)
    ]
    for s, rows in test_cases:
        res = sol.convert(s, rows)
        print(f"s={repr(s)}, rows={rows} → {repr(res)}")


</code></pre>
<p> Leetcode 0006 Solution</p>
</section>

<section data-auto-animate>
<h2 data-id="code-title">Pretty Code</h2>
<pre data-id="code-animation2"><code class="hljs javascript" data-trim data-line-numbers>
import { useState } from 'react';

function Example() {
  const [count, setCount] = useState(0);

  return (

      ...

  );
}
</code></pre>
<p>
Code syntax highlighting courtesy of
<a href="https://highlightjs.org/usage/">highlight.js</a>.
</p>
</section>

<section data-auto-animate>
<h2 data-id="code-title">With Animations</h2>
<pre
data-id="code-animation2"
><code class="hljs javascript" data-trim data-line-numbers="|4,8-11|17|22-24"><script type="text/template">
import { useState } from 'react';

function Example() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}

function SecondExample() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}
</script></code></pre>
</section>


{{< /reveal >}}


