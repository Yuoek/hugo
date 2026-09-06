---
title: DOM
date: 2026-09-05
description: "Javascript 教程"
categories: ["Program", "JavaScript"]
series: ["Javascript 学习记录"]
series_order: 17
---


<!-- mtoc-start -->

* [getElementById() 方法](#getelementbyid-方法)

<!-- mtoc-end -->

## getElementById() 方法

```js
```
  <button onclick="accessEle()">接受</button>
  <p id="output"></p>
  <script>
    function accessEle() {
      document.getElementById("output").innerHTML = 
        "你好呀，你刚刚点击了按钮哦";
    }
  </script>
