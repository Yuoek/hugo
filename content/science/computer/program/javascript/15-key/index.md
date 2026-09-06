---
title: 重要的关键字
date: 2026-09-05
description: "Javascript 教程"
categories: ["Program", "JavaScript"]
series: ["Javascript 学习记录"]
series_order: 16
---


<!-- mtoc-start -->

* [this](#this)

<!-- mtoc-end -->

## this

```js
  <div id="key"></div>
  <script>
    const output = document.getElementById("key");
    var num = 10;
    function printNum() {
      output.innerHTML += "内部函数：" + num + "<br>";
    }
    this.printNum();
    output.innerHTML += "外部函数：" + this.num + "<br>";
  </script>
```
