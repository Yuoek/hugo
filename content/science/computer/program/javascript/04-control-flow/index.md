---
title: 流程控制
date: 2026-09-03
description: "Javascript 教程"
categories: ["Program", "JavaScript"]
series: ["Javascript 学习记录"]
series_order: 5
---


<!-- mtoc-start -->

* [if-else](#if-else)
  * [if](#if)
  * [if-else](#if-else-1)
  * [if-else-if](#if-else-if)
* [while](#while)
  * [do-while](#do-while)
  * [while](#while-1)
  * [for-in](#for-in)
  * [for-of](#for-of)
* [break](#break)
* [continue](#continue)
* [switch case](#switch-case)

<!-- mtoc-end -->

## if-else

### if

### if-else
```js
  <div id="if-loop"></div>
  <script>
    let result;
    let age = 25;
    if(age >= 18) {
      result = "你已经成年啦";
    } else {
      result = "你还没有成年哦";
    }
    document.getElementById("if-loop").innerHTML = result;
  </script>
```

### if-else-if

## while

### do-while
```js
  <div id="do-while-loop"></div>
  <script type="text/javascript">
    let output2 = document.getElementById("do-while-loop");
    var count = 0;
    output2.innerHTML += "do-while 循环中";
    do {
      output2.innerHTML += "循环 " + count + "次" + "<br>";
      count++;
    }
    while(count < 10);
    output2.innerHTML += "循环结束";
  </script>
```

### while
```js
  <div id="output"></div>
  <script type="text/javascript">
    let output = document.getElementById("output");
    var count = 0;
    output.innerHTML += "while 循环中";
    while(count < 10) {
      output.innerHTML += "循环 " + count + "次" + "<br>";
      count++;
    }
    output.innerHTML += "循环结束";
  </script>
```


### for-in
```js
  <p id="for-in-loop"></p>
  <script>
    let output3 = document.getElementById("for-in-loop");
    let yu = {
      name: "虞ok",
      age: 17,
      love: true,
    }
    for(u in yu) {
      output3.innerHTML += u + "-->" + yu[u] + ";";
    }
  </script>
```

### for-of
```js
  <p id="for-of-loop"></p>
  <script>
    const output4 = document.getElementById("for-of-loop");
    // 数组
    output4.innerHTML += "数组：<br>";
    const arr = ["javascript", "c", "cpp", "python", "haskell"];
    for(let ele of arr) {
      output4.innerHTML += ele + ";";
    }

    // 字符串
    output4.innerHTML += "<br>字符串：<br>";
    const str = "Dear Yuoek";
    for(let char of str) {
      output4.innerHTML += char + ";";
    }

    // 集合
    output4.innerHTML += "<br>集合：<br>";
    const nums = new Set([1, 2, 3, 4]);
    for(let num of nums) {
      output4.innerHTML += num + ";";
    }

    // 字典
    output4.innerHTML += "<br>字典：<br>";
    const map = new Map();
    map.set("a", 1);
    map.set("b", 2);
    map.set("c", 3);
    for(let [k, v] of map) {
      output4.innerHTML += k + "-->" + v + ";";
    }
  </script>
```

## break

## continue

## switch case
