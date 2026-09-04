---
title: Placement
date: 2026-09-03
description: "Javascript 教程"
categories: ["Program", "JavaScript"]
series: ["Javascript 学习记录"]
series_order: 2
---

## 引用

使用 script 标签
```html
<script>
```

在 head 内
```html
  <script>
    function hi() {
      alert("Hello, Yuoek")
    }
  </script>
```

在 body 内
```html
  <script type="text/javascript">
    document.write("Dear Yuoek:")
  </script>
```

在 head 和 body 内
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Yuoek</title>
  <script>
    function hi() {
      alert("Hello, Yuoek")
    }
  </script>
</head>
<body>
  <h1>Yuoek</h1>
  <input type="<button" onclick="hi()" value="sayHi">

  <br>
  <script type="text/javascript">
    document.write("Dear Yuoek:")
  </script>

  <p>要积极做项目</p>
</body>
</html>
```

外部引用

创建 yuoek.js
```javascript
function yu() {
    alter("Dear Yuoek!")
}
```

在 index.html <head> 内引用
```html
<script type="text/javascritp" src="yuoek.js"></script>
```
