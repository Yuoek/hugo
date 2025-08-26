---
title: "Hugo 添加音乐"
date: 2025-08-24T09:30:28+08:00
description: ""
categories: ["Study", "Hugo"]
tags: ["Study","Hugo"]
series: ["Hugo 学习记录"]
series_order: 3
type: "posts"
---

<!-- require APlayer -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/aplayer/dist/APlayer.min.css">
<script src="https://cdn.jsdelivr.net/npm/aplayer/dist/APlayer.min.js"></script>
<!-- require MetingJS -->
<script src="https://cdn.jsdelivr.net/npm/meting@2/dist/Meting.min.js"></script>

### chart 18

{{< chart >}}
type: 'radar',
         data: {
            labels: ["HTML", "CSS", "JAVASCRIPT", "CHART.JS", "JQUERY", "BOOTSTRP"],
            datasets: [{
               label: "online tutorial subjects",
               data: [20, 40, 33, 35, 30, 38],
               backgroundColor: ['lightgrey'],
               pointBackgroundColor: ['yellow', 'aqua', 'pink', 'lightgreen', 'lightblue', 'gold'],
               borderColor: ['black'],
               borderWidth: 1,
               pointRadius: 6,
            }],
         },
         options: {
            responsive: false,
            scales: {
               r: {
                  suggestedMin: 40,
                  suggestedMax: 40
               }
            }
         }
{{< /chart >}}

### chart 17 

{{< chart >}}
type: 'bar',
         data: {
            labels: ["HTML", "CSS", "JAVASCRIPT", "CHART.JS", "JQUERY", "BOOTSTRP"],
            datasets: [{
               label: "online tutorial subjects",
               data: [20, 40, 30, 35, 30, 20],
               backgroundColor: ['yellow', 'aqua', 'pink', 'lightgreen', 'lightblue', 'gold'],
               borderColor: ['black'],
               borderWidth: 1,
               pointRadius: 4,
            }],
         },
         options: {
            responsive: false,
            scales: {
               x: {
                  min: 'CSS',
                  max: 'JQUERY'
               }
            }
         }
{{< /chart >}}


### chart 16 

{{< chart >}}
type: 'bar',
         data: {
            labels: ["HTML", "CSS", "JAVASCRIPT", "CHART.JS", "JQUERY", "BOOTSTRP"],
            datasets: [{
               label: "online tutorial subjects",
               data: [20, 40, 30, 35, 30, 20],
               backgroundColor: ['coral', 'aqua', 'pink', 'lightgreen', 'lightblue', 'crimson'],
               borderColor: ['black'],
               borderWidth: 1,
               pointRadius: 4,
            }],
         },
         options: {
            responsive: false,
            indexAxis: 'y',
            scales: {
               x: {
                  grid: {
                     color: 'orange',
                     borderColor: 'orange',
                  }
               }
            }
         }
{{< /chart >}}


### chart 15 

{{< chart >}}
type: 'scatter',
         data: {
            labels: ["HTML", "CSS", "JAVASCRIPT", "CHART.JS", "JQUERY", "BOOTSTRP"],
            datasets: [{
                  type: 'scatter',
                  label: "online tutorial subjects",
                  data: [
                     {x:10, y:14},
                     {x:25, y:35},
                     {x:21, y:20},
                     {x:35, y:28},
                     {x:15, y:10},
                     {x:19, y:30}
                  ],
                  backgroundColor: ['yellow', 'aqua', 'pink', 'lightgreen', 'gold', 'lightblue'],
                  borderColor: ['black'],
                  radius: 8,
               },
               {
                  type: 'polarArea',
                  label: "online tutorial exam",
                  data: [20, 40, 30, 35, 30, 20],
                  backgroundColor: ['navy', 'aqua', 'pink', 'lightgreen', 'lightblue', 'gold'],
                  borderColor: ['black'],
                  borderWidth: 2,
                  pointRadius: 5,
               }
            ],
         },
         options: {
            responsive: false,
            scales: {
               y: {
                  beginAtZero: true
               }
            }
         }
{{< /chart >}}

### chart 14 

{{< chart >}}
type: 'scatter',
         data: {
            labels: ["HTML", "CSS", "JAVASCRIPT", "CHART.JS", "JQUERY", "BOOTSTRP"],
            datasets: [{
               label: "online tutorial subjects",
               data: [
                  {x:10, y:14},
                  {x:25, y:35},
                  {x:21, y:20},
                  {x:35, y:28},
                  {x:15, y:10},
                  {x:19, y:30},
               ],
               backgroundColor: ['yellow', 'aqua', 'pink', 'lightgreen', 'gold', 'lightblue'],
               borderColor: ['black'],
               radius: 8,
            }],
         },
         options: {
            responsive: false,
            scales: {
               x: {
                  type: 'linear',
                  position: 'bottom,'
               }
            }
         }
{{< /chart >}}

### chart 13 

{{< chart >}}
type: 'bubble',
         data: {
            labels: ["HTML", "CSS", "JAVASCRIPT", "CHART.JS", "JQUERY", "BOOTSTRP"],
            datasets: [{
               label: "online tutorial subjects",
               data: [{
                     x: 20,
                     y: 21,
                     z: 20
                  },
                  {
                     x: 25,
                     y: 25,
                     z: 25
                  },
                  {
                     x: 13,
                     y: 11,
                     z: 25
                  },
                  {
                     x: 40,
                     y: 18,
                     z: 25
                  },
                  {
                     x: 31,
                     y: 28,
                     z: 25
                  },
                  {
                     x: 27,
                     y: 35,
                     z: 35
                  }
               ],
               backgroundColor: ['yellow', 'aqua', 'pink', 'lightgreen', 'gold', 'lightblue'],
               borderColor: ['black'],
               radius: 8,
            }],
         },
         options: {
         responsive: false,
         }
{{< /chart >}}

### chart 12 

{{< chart >}}
type: 'polarArea',
         data: {
            labels: ["HTML", "CSS", "JAVASCRIPT", "CHART.JS", "JQUERY", "BOOTSTRP"],
            datasets: [{
               label: "online tutorial subjects",
               data: [20, 40, 15, 35, 25, 38],
               backgroundColor: ['yellow', 'aqua', 'pink', 'lightgreen', 'gold', 'lightblue'],
            }],
         },
         options: {
            responsive: false,
         }
{{< /chart >}}

### chart 11 

{{< chart >}}
type: 'pie',
         data: {
            labels: ["HTML", "CSS", "JAVASCRIPT", "CHART.JS", "JQUERY", "BOOTSTRP"],
            datasets: [{
               label: "online tutorial subjects",
               data: [20, 40, 13, 35, 20, 38],
               backgroundColor: ['yellow', 'aqua', 'pink', 'lightgreen', 'gold', 'lightblue'],
               hoverOffset: 5
            }],
         },
         options: {
            responsive: false,
         }
{{< /chart >}}

### chart 10 

{{< chart >}}
type: 'doughnut',
         data: {
            labels: ["HTML", "CSS", "JAVASCRIPT", "CHART.JS", "JQUERY", "BOOTSTRP"],
            datasets: [{
            label: "online tutorial subjects",
            data: [20, 40, 13, 35, 20, 38],
            backgroundColor: ['yellow', 'aqua', 'pink', 'lightgreen', 'gold', 'lightblue'],
            hoverOffset: 5
            }],
         },
         options: {
            responsive: false,
         }
{{< /chart >}}

### chart 9 

{{< chart >}}
type: 'radar',
         data: {
            labels: ["HTML", "CSS", "JAVASCRIPT", "CHART.JS", "JQUERY", "BOOTSTRP"],
            datasets: [{
               label: "online tutorial subjects",
               data: [20, 40, 33, 35, 30, 38],
               backgroundColor: ['lightgrey'],
               pointBackgroundColor: ['yellow', 'aqua', 'pink', 'lightgreen', 'lightblue', 'gold'],
               borderColor: ['black'],
               borderWidth: 1,
               pointRadius: 6,
            }],
         },
         options: {
            responsive: false,
            elements: {
               line: {
                  borderWidth: 3
               }
            }
         }
{{< /chart >}}

### chart 8 
{{< chart >}}
type: 'bar',
         data: {
            labels: ["HTML", "CSS", "JAVASCRIPT", "CHART.JS", "JQUERY", "BOOTSTRP"],
            datasets: [{
               label: "online tutorial subjects",
               data: [20, 40, 30, 35, 30, 20],
               backgroundColor: ['coral', 'aqua', 'pink', 'lightgreen', 'lightblue', 'crimson'],
               borderColor: ['red', 'blue', 'fuchsia', 'green', 'navy', 'black'],
               borderWidth: 2,
            }],
         },
         options: {
            responsive: false,
            plugins: {
               tooltip: {
                  enabled: true,
                  usePointStyle: true,
                  titleAlign: 'center',
                  titleColor: 'gold',
                  titleSpacing: 3,
                  TitleFont: {
                     weight: 'bold'
                  },
                  backgroundColor: 'midnightblue',
                  bodyColor: 'orange',
                  bodyAlign: 'center',
                  bodyFont: {
                     weight: 'italic'
                  },
                  callbacks: {
                     labelPointStyle: function(context) {
                        return {
                           pointStyle: 'circle',
                           rotation: 0
                        };
                     },
                  }
               }
            }
         },
{{< /chart >}}

### 修改 Chart-js 显示大小

> 在 hugo 博客中引用 chartjs 的简码如下，
> 修改 css 样式，使其图表大小正常
> 将修改好的代码返回保存在 custom.css 中

```css
/* custom.css */
.chart-container {
    position: relative;
    height: 400px;
    width: 100%;
}

canvas {
    display: block;
    max-width: 100%;
    height: 400px !important;
    width: 100% !important;
}
```

**修改说明：**
1. 为图表容器设置了固定高度400px和100%宽度
2. 为canvas元素设置了最大宽度100%和固定高度400px
3. 使用!important确保样式优先级覆盖Chart.js的默认样式
4. 移除了原代码中的`responsive: false`选项（建议在简码中改为`responsive: true`）

**建议同时修改简码中的选项：**

````markdown

{{\< chart >}}
type: "line",
data: {
    // ... 数据保持不变
},
options: {
    responsive: true,  // 改为true以启用响应式
    maintainAspectRatio: false,  // 添加此选项
    // ... 其他选项保持不变
}
{{\< /chart >}}
````

---

### Chart 7

{{< chart >}}
type: "line",
         data: {
            labels: ["HTML", "CSS", "JAVASCRIPT", "CHART.JS", "JQUERY", "BOOTSTRP"],
            datasets: [{
            label: "online tutorial subjects",
            data: [20, 40, 30, 35, 30, 20],
            backgroundColor: ['coral', 'aqua', 'pink', 'lightgreen', 'lightblue', 'crimson'],
            borderColor: [
            "black",
            ],
            borderWidth: 1,
            pointRadius: 5,
            }],
         },
         options: {
            responsive: false,
            animations: {
               tension: {
               duration: 750,
               easing: 'easeInBounce',
               from: 1,
               to: 0,
               loop: true
               }
            },
            scales: {
               y: {
                  min: 0,
                  max: 45,
               }
            }
         }
{{< /chart >}}

### chart 6 

{{< chart >}}
type: "line",
         data: {
            labels: ["HTML", "CSS", "JAVASCRIPT", "CHART.JS", "JQUERY", "BOOTSTRP"],
            datasets: [{
               label: "online tutorial subjects",
               data: [20, 40, 30, 35, 30, 20],
               backgroundColor: ['coral', 'aqua', 'pink', 'lightgreen', 'lightblue', 'crimson'],
               borderColor: [
                  "black",
               ],
               borderWidth: 1,
               pointRadius: 5,
            }],
         },
         options: {
               responsive: false,
               plugins: {
                  legend: {
                     display: true,
                     position: 'bottom',
                     align: 'center',
                     labels: {
                        color: 'darkred',
                        font: {
                           weight: 'bold'
                        },
                     }
                  }
               }
            }
{{< /chart >}}


## Meting 插入

```markdown

## 网易云

<meting-js
    server="netease"
    type="playlist"
    id="433959725"
    mutex="true"
    fixed="true">
</meting-js>

<meting-js
    auto="https://y.qq.com/n/yqq/song/001RGrEX3ija5X.html">
</meting-js>

## QQ 音乐

<meting-js
    auto="https://y.qq.com/n/yqq/song/001RGrEX3ija5X.html">
</meting-js>


## 酷狗

<meting-js
    server="kugou"
    type="playlist"
    id="29y7n5e"
    mutex="true">
</meting-js>

<meting-js
    name="yuoek"
    artist="sophie"
    url="/musickugou/kugou/song2.mp3"
    cover="/img/197-sandbox1.png"
    mutex="true">
</meting-js>

<meting-js
    server="kugou"
    type="album"
    id="100260930">
</meting-js>


## 本地 

<meting-js
    name="rainymood"
    artist="rainymood"
    url="/musickugou/kugou/song.mp3"
    cover="/img/197-sandbox1.png"
    lrc="/musickugou/kugou/song.lrc" 
    autoplay="true"
    loop="false"
    fixed="true"
    mini="true"
    mutex="true">
</meting-js>
```


## Meting 参数设置
| 选项 | 默认值 | 描述 |
| --------------- | --------------- | --------------- |
| option	|	default	|	description |
| id	|	require	|	song id / playlist id / album id / search keyword   |
| server	|	require	|	music platform: netease, tencent, kugou, xiami, baidu   |
| type	|	require	|	song, playlist, album, search, artist   |
| auto	|	options	|	music link, support: netease, tencent, xiami    |
| fixed	|	false	|	enable fixed mode   |
| mini	|	false	|	enable mini mode    |
| autoplay	|	false	|	audio autoplay  |
| theme	|	#2980b9	| main color  |
| loop	|	all	|	player loop play, values: 'all', 'one', 'none'  |
| order	|	list	|	player play order, values: 'list', 'random' |
| preload	|	auto	|	values: 'none', 'metadata', 'auto'  |
| volume	|	0.7	| default volume, notice that player will remember user setting, default volume will not work after user set volume themselves    |
| mutex	|	true	|	prevent to play multiple player at the same time, pause other players when this player start play   |
| lrc-type	|	0	| lyric type  |
| list-folded	|	false	|	indicate whether list should folded at first    |
| list-max-height	|	340px	|	list max height     |
| storage-name	|	metingjs	|	localStorage key that store player setting  |


