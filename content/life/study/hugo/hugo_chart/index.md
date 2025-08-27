---
title: "Hugo Chart 图表"
date: 2025-08-27T15:13:54+08:00
description: ""
categories: ["Study", "Hugo"]
tags: ["Study","Hugo"]
series: ["Hugo 学习记录"]
series_order: 5
type: "posts"
---









## 示例


### chart 1

{{< chart >}}
type: 'line',
data: {
  labels: ['tomato', 'blueberry', 'banana', 'lime', 'orange'],
  datasets: [{
    label: '# of votes',
    data: [12, 19, 3, 5, 3],
  }]
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

### Chart 2

{{< chart >}}
type: 'bar',
data: {
   labels: ["HTML", "CSS", "JAVASCRIPT", "CHART.JS", "JQUERY", "BOOTSTRP"],
   datasets: [{
      label: "Online Tutorial Subjects",
      data: [20, 40, 30, 35, 30, 20],
   }],
},
options: {
    responsive: false,
}
{{< /chart >}}

### chart 3 

{{< chart >}}
type: 'bar',
         data: {
            labels: ["HTML", "CSS", "JAVASCRIPT", "CHART.JS", "JQUERY", "BOOTSTRP"],
            datasets: [{
               label: "online tutorial subjects",
               data: [20, 40, 30, 35, 30, 20],
               backgroundColor: ['yellow', 'aqua', 'pink', 'lightgreen', 'lightblue', 'gold'],
               borderColor: ['red', 'blue', 'fuchsia', 'green', 'navy', 'black'],
               borderWidth: 2,
            }],
         },
         options: {
            responsive: false,
         }
{{< /chart >}}

### chart 4 
{{< chart >}}
type: 'bar',
         data: {
            labels: ["HTML", "CSS", "JAVASCRIPT", "CHART.JS", "JQUERY", "BOOTSTRP"],
            datasets: [{
            label: "online tutorial subjects",
            data: [20, 40, 30, 35, 30, 20],
            backgroundColor: ['yellow', 'aqua', 'pink', 'lightgreen', 'lightblue', 'gold'],
            borderColor: ['red', 'blue', 'fuchsia', 'green', 'navy', 'black'],
            borderWidth: 2,
            }],
         },
         options: {
            responsive: false,
            layout: {
               padding: {
                  left: 40,
                  right: 40,
               }
            },
            plugins: {
               legend: {
                  labels: {
                     font: {
                        size: 25,
                        family: 'Helvetica',
                        style: 'bold',
                     }
                  }
               }
            }
         }
{{< /chart >}}


### chart 5 

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
            events: ['click'],
            interaction: {
               mode: 'nearest',
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

## KaTex 

{{< katex >}}
% KaTeX inline notation
Inline notation: \(\varphi = \dfrac{1+\sqrt5}{2}= 1.6180339887…\)

\[\begin{aligned}
\nabla \times \vec{\mathbf{B}} - \frac{1}{c} \frac{\partial \vec{\mathbf{E}}}{\partial t} &= \frac{4\pi}{c} \vec{\mathbf{j}} \\
\nabla \cdot \vec{\mathbf{E}} &= 4\pi \rho \\
\nabla \times \vec{\mathbf{E}} + \frac{1}{c} \frac{\partial \vec{\mathbf{B}}}{\partial t} &= \vec{\mathbf{0}} \\
\nabla \cdot \vec{\mathbf{B}} &= 0
\end{aligned}\]

锵锵锵！今年的第二篇季度总结来了！不知不觉地就写了很多字，感觉其中大半部分都是在吐槽我的打工经历……以及吐槽一些片子。这几个月总算把旷野之息通关啦，但是游戏进度只有百分之二十几，啊，似乎漏了很多任务没做……但是我已经沉迷于王国之泪了！！这几个月发生了不少事情，也消耗了很多精力。

$$ 
\LaTeX
$$

\(\textcolor{#228B22}{F=ma}\)


{{< chart >}}
  labels: generateLabels(),
  datasets: [
    {
      label: 'D0',
      data: generateData(),
      borderColor: Utils.CHART_COLORS.red,
      backgroundColor: Utils.transparentize(Utils.CHART_COLORS.red),
      hidden: true
    },
    {
      label: 'D1',
      data: generateData(),
      borderColor: Utils.CHART_COLORS.orange,
      backgroundColor: Utils.transparentize(Utils.CHART_COLORS.orange),
      fill: '-1'
    },
    {
      label: 'D2',
      data: generateData(),
      borderColor: Utils.CHART_COLORS.yellow,
      backgroundColor: Utils.transparentize(Utils.CHART_COLORS.yellow),
      hidden: true,
      fill: 1
    },
    {
      label: 'D3',
      data: generateData(),
      borderColor: Utils.CHART_COLORS.green,
      backgroundColor: Utils.transparentize(Utils.CHART_COLORS.green),
      fill: '-1'
    },
    {
      label: 'D4',
      data: generateData(),
      borderColor: Utils.CHART_COLORS.blue,
      backgroundColor: Utils.transparentize(Utils.CHART_COLORS.blue),
      fill: '-1'
    },
    {
      label: 'D5',
      data: generateData(),
      borderColor: Utils.CHART_COLORS.grey,
      backgroundColor: Utils.transparentize(Utils.CHART_COLORS.grey),
      fill: '+2'
    },
    {
      label: 'D6',
      data: generateData(),
      borderColor: Utils.CHART_COLORS.purple,
      backgroundColor: Utils.transparentize(Utils.CHART_COLORS.purple),
      fill: false
    },
    {
      label: 'D7',
      data: generateData(),
      borderColor: Utils.CHART_COLORS.red,
      backgroundColor: Utils.transparentize(Utils.CHART_COLORS.red),
      fill: 8
    },
    {
      label: 'D8',
      data: generateData(),
      borderColor: Utils.CHART_COLORS.orange,
      backgroundColor: Utils.transparentize(Utils.CHART_COLORS.orange),
      fill: 'end',
      hidden: true
    },
    {
      label: 'D9',
      data: generateData(),
      borderColor: Utils.CHART_COLORS.yellow,
      backgroundColor: Utils.transparentize(Utils.CHART_COLORS.yellow),
      fill: {above: 'blue', below: 'red', target: {value: 350}}
    }
  ]
{{< /chart >}}


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


