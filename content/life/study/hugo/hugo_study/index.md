---
title: "Hugo 学习之旅"
date: 2025-08-23T21:02:02+08:00
mermaid: true
description: ""
categories: ["Study", "Hugo"]
tags: ["Study","Hugo"]
series: ["Hugo 学习记录"]
series_order: 2
type: "posts"
---

<!-- require APlayer -->
<link rel="stylesheet" href="/renderjs/aplayer/dist/APlayer.min.css">
<script src="/renderjs/aplayer/dist/APlayer.min.js"></script>
<!-- require MetingJS -->
<script src="/renderjs/meting/dist/Meting.min.js"></script>



<meting-js
    name="I Really Want to Stay at Your House"
    artist="Rosa Walton_Hallie Coggins"
    url="/voice/kugou/sophieSong/I Really Want to Stay at Your House - Rosa Walton_Hallie Coggins/I Really Want to Stay at Your House.mp3 "
    cover="/voice/kugou/sophieSong/I Really Want to Stay at Your House - Rosa Walton_Hallie Coggins/cyberpunk_lucy_moon.jpg"
    lrc="/voice/kugou/sophieSong/I Really Want to Stay at Your House - Rosa Walton_Hallie Coggins/I Really Want to Stay at Your House_合并歌词.lrc" 
    autoplay="false"
    loop="false"
    mutex="true">
</meting-js>


## **添加** mermaid 

### 添加 mermaid.html 

1. 在 Hugo 博客根目录下的 `layouts` 目录下新建 `partials\mermaid.html` (<u>注：如果没有该目录则按步骤新建该目录</u>)，如下：  
```bash
layouts  
|_____partials  
|     |______mermaid.html   

```
2. 在 `mermaid.html` 添加以下内容：  
```html
<!-- mermaid.html -->
{{ if .Params.mermaid }}  <!-- 判断是否开启 -->
<script type="module">  
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.esm.min.mjs'; 
    mermaid.initialize({ 
        startOnLoad: true,
        theme: 'default',
        // 添加以下配置项调整图表大小
        flowchart: {
            useMaxWidth: false,  // 禁用最大宽度限制
            htmlLabels: true,
            curve: 'basis'
        }
    });  
</script>  
<script>  
    // Replace mermaid pre.code to div  
    Array.from(document.getElementsByClassName("language-mermaid")).forEach(  
        (el) => {  
            el.parentElement.outerHTML = `<div class="mermaid">${el.innerHTML}</div>`;  
        }  
    );  
</script>  
<style>  
    /* 设置mermaid图表样式 */
    .mermaid {
        overflow: auto;  /* 添加滚动条以防图表过大 */
        text-align: center;
        margin: 1rem 0;
    }
    
    /* 设置svg大小适应容器 */
    .mermaid svg {  
        display: block;  
        margin: auto;
        max-width: 100%;  /* 确保不超过容器宽度 */
        height: auto;     /* 保持宽高比 */
    }  
    
    /* 可选：针对特定类型图表调整 */
    .mermaid .flowchart-link {
        stroke-width: 2px;
    }
</style>  
{{ end }}
```

~~(`PS:` 刚刚使用代码块时发现没有行号，参考别人的教程显示了行号，但复制代码块时连行号也一起复制了，所以还是选择没有行号吧 ):~~ 用 AI 修改已能正常复制代码💡2025-08-26 09:31。

- 上面代码在别人原有的代码上经过 `AI` 加工。其中 第 4 行：
```html
import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.esm.min.mjs'

```

- 可以引用本地 `mermaid` js, 引用如下:
```html
import mermaid from 'renderjs/mermaid/mermaid.esm.min.mjs'

```

### 本地引用 mermaid

1. 在引用本地 `mermaid` js 前，先在博客根目录 `static\` 创建 `renderjs` (或其它名称的文件) 用来存放 `mermaid` js 包。
```bash
|static
|_______renderjs
|       
```

2. 进入到 `renderjs` 目录，`npm` 下载 `mermaid`：
```bash
npm i mermaid

```

3. 下载好之后我发现当前目录多了一个文件夹 `node_module`, 进入文件夹找到 `mermaid` 后复制到 `static\` 目录下，复制后的目录如下：
```bash
|static
|_______renderjs
|       |_______mermaid
|               |_______dist
|               |_______mermaid.esm.min.mjs

```

### 复制 `single.html` 并修改

1. 从主题 (目前用的 blowfish) 下的 `layouts\_default\single.html` 复制到 博客目录 `layouts\_default\` 下：
```bash 
|layouts
|   |___ _default
|        |_____single.html 
|
|themes 
|   |_____blowfish 
|         |_____layouts
|               |_____ _default 
|                      |______single.html    
|

```

2. 修改复制后的 `single.html`, 找到`{{ .Content }}` 并在下面添加一行如下：
```html{{ .Content }}
{{ .Content }}
{{- partial "mermaid.html" . -}}
```

### 新建文章引用 `mermaid` 

1. 新建文档 mermaid.md 并添加头文件如下：
```markdown
---
title: "mermaid"
date: 2025-08-24
mermaid: true
---
```

2. 完整示例

````markdown
---
title: "mermaid"
date: 2025-08-24
mermaid: true
---

## 这是 mermaid示例

```mermaid
erDiagram
    CAR {
        string registrationNumber
        string make
        string model
    }
    PERSON {
        string firstName
        string lastName
        int age
    }
    PERSON:::foo ||--|| CAR : owns
    PERSON o{--|| HOUSE:::bar : has

    classDef default fill:#f9f,stroke-width:4px
    classDef foo stroke:#f00
    classDef bar stroke:#0f0
    classDef foobar stroke:#00f
```

````


3. 示例渲染如下:


```mermaid
erDiagram
    CAR {
        string registrationNumber
        string make
        string model
    }
    PERSON {
        string firstName
        string lastName
        int age
    }
    PERSON:::foo ||--|| CAR : owns
    PERSON o{--|| HOUSE:::bar : has

    classDef default fill:#f9f,stroke-width:4px
    classDef foo stroke:#f00
    classDef bar stroke:#0f0
    classDef foobar stroke:#00f
```

可以看到博客文章已经渲染出来 mermaid 图形了，大功告成！！！


## 其它示例

### erDiagram

```mermaid 

erDiagram
    CAR ||--o{ NAMED-DRIVER : allows
    CAR {
        string registrationNumber PK
        string make
        string model
        string[] parts
    }
    PERSON ||--o{ NAMED-DRIVER : is
    PERSON {
        string driversLicense PK "The license #"
        string(99) firstName "Only 99 characters are allowed"
        string lastName
        string phone UK
        int age
    }
    NAMED-DRIVER {
        string carRegistrationNumber PK, FK
        string driverLicence PK, FK
    }
    MANUFACTURER only one to zero or more CAR : makes

```


### quadrantChart


```mermaid


quadrantChart
  title Reach and engagement of campaigns
  x-axis Low Reach --> High Reach
  y-axis Low Engagement --> High Engagement
  quadrant-1 We should expand
  quadrant-2 Need to promote
  quadrant-3 Re-evaluate
  quadrant-4 May be improved
  Campaign A: [0.9, 0.0] radius: 12
  Campaign B:::class1: [0.8, 0.1] color: #ff3300, radius: 10
  Campaign C: [0.7, 0.2] radius: 25, color: #00ff33, stroke-color: #10f0f0
  Campaign D: [0.6, 0.3] radius: 15, stroke-color: #00ff0f, stroke-width: 5px ,color: #ff33f0
  Campaign E:::class2: [0.5, 0.4]
  Campaign F:::class3: [0.4, 0.5] color: #0000ff
  classDef class1 color: #109060
  classDef class2 color: #908342, radius : 10, stroke-color: #310085, stroke-width: 10px
  classDef class3 color: #f00fff, radius : 10

```
### stateDiagram-v2

```mermaid

    stateDiagram-v2
        State1: The state with a note
        note right of State1
            Important information! You can write
            notes.
        end note
        State1 --> State2
        note left of State2 : This is the note to the left.

```

### xychart-beta

```mermaid

xychart-beta
    title "Sales Revenue"
    x-axis [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]
    y-axis "Revenue (in $)" 4000 --> 11000
    bar [5000, 6000, 7500, 8200, 9500, 10500, 11000, 10200, 9200, 8500, 7000, 6000]
    line [5000, 6000, 7500, 8200, 9500, 10500, 11000, 10200, 9200, 8500, 7000, 6000]

```

### flowchart

```mermaid

flowchart TD
    B["fa:fa-twitter for peace"]
    B-->C[fa:fa-ban forbidden]
    B-->D(fa:fa-spinner)
    B-->E(A fa:fa-camera-retro perhaps?)

```

```mermaid

flowchart TD
    A@{ shape: bolt, label: "Communication link" }

```

```mermaid


sequenceDiagram
    participant Alice
    participant Bob
    Alice->>John: Hello John, how are you?
    loop HealthCheck
        John->>John: Fight against hypochondria
    end
    Note right of John: Rational thoughts <br/>prevail!
    John-->>Alice: Great!
    John->>Bob: How about you?
    Bob-->>John: Jolly good!

```

### git Graph

```mermaid

    gitGraph
       commit
       commit
       branch develop
       commit
       commit
       commit
       checkout main
       commit
       commit

```

```mermaid 

erDiagram
    direction TB
    CAR:::someclass {
        string registrationNumber
        string make
        string model
    }
    PERSON:::someclass {
        string firstName
        string lastName
        int age
    }
    HOUSE:::someclass

    classDef someclass fill:#f96

```

```mermaid 

---
config:
  logLevel: 'debug'
  theme: 'base'
  gitGraph:
    showBranches: false
---
      gitGraph
        commit
        branch hotfix
        checkout hotfix
        commit
        branch develop
        checkout develop
        commit id:"ash" tag:"abc"
        branch featureB
        checkout featureB
        commit type:HIGHLIGHT
        checkout main
        checkout hotfix
        commit type:NORMAL
        checkout develop
        commit type:REVERSE
        checkout featureB
        commit
        checkout main
        merge hotfix
        checkout featureB
        commit
        checkout develop
        branch featureA
        commit
        checkout develop
        merge hotfix
        checkout featureA
        commit
        checkout featureB
        commit
        checkout develop
        merge featureA
        branch release
        checkout release
        commit
        checkout main
        commit
        checkout release
        merge main
        checkout develop
        merge release

```

### C4Context

```mermaid 

    C4Context
      title System Context diagram for Internet Banking System
      Enterprise_Boundary(b0, "BankBoundary0") {
        Person(customerA, "Banking Customer A", "A customer of the bank, with personal bank accounts.")
        Person(customerB, "Banking Customer B")
        Person_Ext(customerC, "Banking Customer C", "desc")

        Person(customerD, "Banking Customer D", "A customer of the bank, <br/> with personal bank accounts.")

        System(SystemAA, "Internet Banking System", "Allows customers to view information about their bank accounts, and make payments.")

        Enterprise_Boundary(b1, "BankBoundary") {

          SystemDb_Ext(SystemE, "Mainframe Banking System", "Stores all of the core banking information about customers, accounts, transactions, etc.")

          System_Boundary(b2, "BankBoundary2") {
            System(SystemA, "Banking System A")
            System(SystemB, "Banking System B", "A system of the bank, with personal bank accounts. next line.")
          }

          System_Ext(SystemC, "E-mail system", "The internal Microsoft Exchange e-mail system.")
          SystemDb(SystemD, "Banking System D Database", "A system of the bank, with personal bank accounts.")

          Boundary(b3, "BankBoundary3", "boundary") {
            SystemQueue(SystemF, "Banking System F Queue", "A system of the bank.")
            SystemQueue_Ext(SystemG, "Banking System G Queue", "A system of the bank, with personal bank accounts.")
          }
        }
      }

      BiRel(customerA, SystemAA, "Uses")
      BiRel(SystemAA, SystemE, "Uses")
      Rel(SystemAA, SystemC, "Sends e-mails", "SMTP")
      Rel(SystemC, customerA, "Sends e-mails to")

      UpdateElementStyle(customerA, $fontColor="red", $bgColor="grey", $borderColor="red")
      UpdateRelStyle(customerA, SystemAA, $textColor="blue", $lineColor="blue", $offsetX="5")
      UpdateRelStyle(SystemAA, SystemE, $textColor="blue", $lineColor="blue", $offsetY="-10")
      UpdateRelStyle(SystemAA, SystemC, $textColor="blue", $lineColor="blue", $offsetY="-40", $offsetX="-50")
      UpdateRelStyle(SystemC, customerA, $textColor="red", $lineColor="red", $offsetX="-50", $offsetY="20")

      UpdateLayoutConfig($c4ShapeInRow="3", $c4BoundaryInRow="1")



```

### mindmap

```mermaid


mindmap
  root((mindmap))
    Origins
      Long history
      ::icon(fa fa-book)
      Popularisation
        British popular psychology author Tony Buzan
    Research
      On effectiveness<br/>and features
      On Automatic creation
        Uses
            Creative techniques
            Strategic planning
            Argument mapping
    Tools
      Pen and paper
      Mermaid


```

### timeline

```mermaid

---
config:
  logLevel: 'debug'
  theme: 'default'
  themeVariables:
    cScale0: '#ff0000'
    cScaleLabel0: '#ffffff'
    cScale1: '#00ff00'
    cScale2: '#0000ff'
    cScaleLabel2: '#ffffff'
---
       timeline
        title History of Social Media Platform
          2002 : LinkedIn
          2004 : Facebook : Google
          2005 : YouTube
          2006 : Twitter
          2007 : Tumblr
          2008 : Instagram
          2010 : Pinterest


```


```mermaid 

---
config:
  sankey:
    showValues: false
---
sankey

Agricultural 'waste',Bio-conversion,124.729
Bio-conversion,Liquid,0.597
Bio-conversion,Losses,26.862
Bio-conversion,Solid,280.322
Bio-conversion,Gas,81.144
Biofuel imports,Liquid,35
Biomass imports,Solid,35
Coal imports,Coal,11.606
Coal reserves,Coal,63.965
Coal,Solid,75.571
District heating,Industry,10.639
District heating,Heating and cooling - commercial,22.505
District heating,Heating and cooling - homes,46.184
Electricity grid,Over generation / exports,104.453
Electricity grid,Heating and cooling - homes,113.726
Electricity grid,H2 conversion,27.14
Electricity grid,Industry,342.165
Electricity grid,Road transport,37.797
Electricity grid,Agriculture,4.412
Electricity grid,Heating and cooling - commercial,40.858
Electricity grid,Losses,56.691
Electricity grid,Rail transport,7.863
Electricity grid,Lighting & appliances - commercial,90.008
Electricity grid,Lighting & appliances - homes,93.494
Gas imports,Ngas,40.719
Gas reserves,Ngas,82.233
Gas,Heating and cooling - commercial,0.129
Gas,Losses,1.401
Gas,Thermal generation,151.891
Gas,Agriculture,2.096
Gas,Industry,48.58
Geothermal,Electricity grid,7.013
H2 conversion,H2,20.897
H2 conversion,Losses,6.242
H2,Road transport,20.897
Hydro,Electricity grid,6.995
Liquid,Industry,121.066
Liquid,International shipping,128.69
Liquid,Road transport,135.835
Liquid,Domestic aviation,14.458
Liquid,International aviation,206.267
Liquid,Agriculture,3.64
Liquid,National navigation,33.218
Liquid,Rail transport,4.413
Marine algae,Bio-conversion,4.375
Ngas,Gas,122.952
Nuclear,Thermal generation,839.978
Oil imports,Oil,504.287
Oil reserves,Oil,107.703
Oil,Liquid,611.99
Other waste,Solid,56.587
Other waste,Bio-conversion,77.81
Pumped heat,Heating and cooling - homes,193.026
Pumped heat,Heating and cooling - commercial,70.672
Solar PV,Electricity grid,59.901
Solar Thermal,Heating and cooling - homes,19.263
Solar,Solar Thermal,19.263
Solar,Solar PV,59.901
Solid,Agriculture,0.882
Solid,Thermal generation,400.12
Solid,Industry,46.477
Thermal generation,Electricity grid,525.531
Thermal generation,Losses,787.129
Thermal generation,District heating,79.329
Tidal,Electricity grid,9.452
UK land based bioenergy,Bio-conversion,182.01
Wave,Electricity grid,19.013
Wind,Electricity grid,289.366

```

### kanban

```mermaid

---
config:
  kanban:
    ticketBaseUrl: 'https://mermaidchart.atlassian.net/browse/#TICKET#'
---
kanban
  Todo
    [Create Documentation]
    docs[Create Blog about the new diagram]
  [In progress]
    id6[Create renderer so that it works in all cases. We also add some extra text here for testing purposes. And some more just for the extra flare.]
  id9[Ready for deploy]
    id8[Design grammar]@{ assigned: 'knsv' }
  id10[Ready for test]
    id4[Create parsing tests]@{ ticket: MC-2038, assigned: 'K.Sveidqvist', priority: 'High' }
    id66[last item]@{ priority: 'Very Low', assigned: 'knsv' }
  id11[Done]
    id5[define getData]
    id2[Title of diagram is more than 100 chars when user duplicates diagram with 100 char]@{ ticket: MC-2036, priority: 'Very High'}
    id3[Update DB function]@{ ticket: MC-2037, assigned: knsv, priority: 'High' }

  id12[Can't reproduce]
    id3[Weird flickering in Firefox]

```

### radar 

```mermaid

---
config:
  radar:
    axisScaleFactor: 0.25
    curveTension: 0.1
  theme: base
  themeVariables:
    cScale0: "#FF0000"
    cScale1: "#00FF00"
    cScale2: "#0000FF"
    radar:
      curveOpacity: 0
---
radar-beta
  axis A, B, C, D, E
  curve c1{1,2,3,4,5}
  curve c2{5,4,3,2,1}
  curve c3{3,3,3,3,3}

```


### treemap

```mermaid 

---
config:
  treemap:
    valueFormat: '$0,0'
---
treemap-beta
"Budget"
    "Operations"
        "Salaries": 700000
        "Equipment": 200000
        "Supplies": 100000
    "Marketing"
        "Advertising": 400000
        "Events": 100000

```


### latex

```mermaid 


 graph LR
      A["$$x^2$$"] -->|"$$\sqrt{x+3}$$"| B("$$\frac{1}{2}$$")
      A -->|"$$\overbrace{a+b+c}^{\text{note}}$$"| C("$$\pi r^2$$")
      B --> D("$$x = \begin{cases} a &\text{if } b \\ c &\text{if } d \end{cases}$$")
      C --> E("$$x(t)=c_1\begin{bmatrix}-\cos{t}+\sin{t}\\ 2\cos{t} \end{bmatrix}e^{2t}$$")

```

---
参考[1]：   
作者：[梧桐碎梦](https://wutongsuimeng.github.io/)   
参考链接：[https://wutongsuimeng.github.io/post/%E7%BB%99hugo%E6%B7%BB%E5%8A%A0mermaid%E6%94%AF%E6%8C%81/](https://wutongsuimeng.github.io/post/%E7%BB%99hugo%E6%B7%BB%E5%8A%A0mermaid%E6%94%AF%E6%8C%81/)  



