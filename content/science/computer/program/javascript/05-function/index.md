---
title: 函数
date: 2026-09-05
description: "Javascript 教程"
categories: ["Program", "JavaScript"]
series: ["Javascript 学习记录"]
series_order: 6
---


<!-- mtoc-start -->

* [定义](#定义)
* [声明](#声明)
* [带参函数](#带参函数)
* [函数参数返回](#函数参数返回)
* [函数作为变量](#函数作为变量)

<!-- mtoc-end -->

## 定义

```js
  <p id="yu"></p>
  <script>
    function yu() {
      const output = document.getElementById("yu");
      output.innerHTML = "Dear Yuoek";
    }
    yu();
  </script>
```

## 声明

```js
  <script>
   const add(3, 4) = function (x, y) {
     document.write(x + y);
   };
  </script>
``` 

## 带参函数

```js
  <p id="sum"></p>
  <script type="text/javascript">
    function add(a, b) {
      const output = document.getElementById("sum");
      let res = a + b;
      let res2 = a + " * " + b + " = " + (a * b)
      // ${} 模板字符串
      output.innerHTML += `${a} + ${b} = ${res}`;
      output.innerHTML += "<br>";
      output.innerHTML += res2;
    }
  </script>
  <input type="button" onclick="add(3, 5)" name="" value="求和">
```

## 函数参数返回

```js
  <script type="text/javascript">
    function concatenate(a, b) {
      var full;
      full = a * b;
      return full;
    }
  </script>
  <script type="text/javascript">
    function callFunction() {
      var res;
      res = concatenate(3, 8);
      alert(res);
    }
  </script>
  <input type="button" onclick="callFunction()" name="" value="函数返回调用">
```

## 函数作为变量

```js
  <p id="value"></p>
  <script>
    const Func = function() {return "Yuoek"};
    document.getElementById("value").innerHTML = "Hello" + "," + Func();
  </script>
```
