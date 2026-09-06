---
title: Web API
date: 2026-09-05
description: "Javascript 教程"
categories: ["Program", "JavaScript"]
series: ["Javascript 学习记录"]
series_order: 13
---


<!-- mtoc-start -->

* [fetch](#fetch)

<!-- mtoc-end -->

## fetch

```js
  <div id="fetch-api"></div>
  <script>
  const URL = 'https://jsonplaceholder.typicode.com/todos/5';
  fetch(URL)
    .then(res => res.json())
    .then(data => {
    document.getElementById("fetch-api").innerHTML += 
    "从 API 获取的 data: " + "<br>" + 
    JSON.stringify(data);
    });
  </script>
```

