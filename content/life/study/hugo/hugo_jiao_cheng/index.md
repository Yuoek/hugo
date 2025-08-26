---
title: "Hugo 教程"
date: 2025-08-25T08:07:33+08:00
description: ""
categories: ["Study", "Hugo"]
tags: ["Study","Hugo"]
series: ["Hugo 学习记录"]
series_order: 4
type: "posts"
---

## Hugo 教程

### 插入 Geogebra 

<!-- **使用方法：** -->
<!-- ```html -->
<!--  geogebra file="geogebra/math1.ggb" >}} -->
<!-- { geogebra file="geogebra/math2.ggb" toolbar="false" >}} -->
<!-- { geogebra file="geogebra/math3.ggb" algebra="false" menubar="false" >}} -->
<!-- ``` -->

{{< geogebra geogebra>}}


{{< geogebra math >}}


{{< geogebra geogebra-test  >}}

### 插入 bilibili 视频 

来源：[https://iubucuoo.github.io/posts/website_video/](https://iubucuoo.github.io/posts/website_video/)

#### 1. 创建 layouts/shortcodes/bilibili.html 

创建 layouts/shortcodes/bilibili.html 

如果没有上述文件，则按目录创建，在 bilibili.html 写入下面代码：

```html 
<!DOCTYPE HTML>
<html>

  <head>
    <!-- style 样式 是为了让网页上的视频框按比例显示而非固定的大小 -->
    <style type="text/css">
      .aspect-ratio {
        position: relative;
        width: 100%;
        height: 0;
        padding-bottom: 75%;
      }

      .aspect-ratio iframe {
        position: absolute;
        width: 100%;
        height: 100%;
        left: 0;
        top: 0;
      }
    </style>
  </head>

  <body>
    <div class="aspect-ratio">
      <iframe
              src="https://player.bilibili.com/player.html?bvid={{.Get 0 }}&page={{ if .Get 1 }}{{.Get 1}}{{ else }}1&high_quality=1&danmaku=0{{end}}&autoplay=0"
              scrolling="no" 
              border="0" 
              frameborder="no" 
              framespacing="0" 
              allowfullscreen="true"
              sandbox="allow-top-navigation allow-same-origin allow-forms allow-scripts"
              >
      </iframe>
      <!-- src 中的 &high_quality=1&danmaku=0 设定了高清程度并默认屏蔽弹幕 -->
      <!-- sandbox 阻止了点击视频中的按钮跳转到B站的行为 -->
    </div>
  </body>

</html>

```

#### 引用 

在 markdown 文章使用短代码如下：

```markdown

## 使用 BV 号 

{{\< bilibili BV1sz4y197L8 >}}  注：前面 /< 加上 `\` 防止渲染，实际为 `<`

## 使用 BV 号 + 集数


{{\< bilibili BV1sz4y197L8 10 >}}

```

#### 使用示例

**BV 号: BV1k23BzRELg**

{{< bilibili BV1k23BzRELg >}}

**BV 号 + 集数: BV1k23BzRELg 10**

{{< bilibili BV1k23BzRELg 10 >}}

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


## 做了什么？

### 1. 打工被坑

> 这个说来话长，在上个季度总结博客里说过这份工的来龙去脉，当时说：
> 于是，这三个月基本都在忙这份工作呢，第一阶段该干的已经干得差不多了，在收尾测试中，所以最近几天才稍微清闲了一点！

那时项目还有一个大的收费模块没做好（需求都没写好）；以及别的功能模块有一些需要二次修改的内容没改，总的来说整个项目完成了大概75%吧，已经完成的部分都已经部署到机器上了，在测试修bug。

这个项目特别草台，尤其是PM，特别不专业，特别浪费我们开发的时间！！本身PM和老板是一个公司里的，而我们只是一个外包开发团队，也就是说我们完全不清楚、也不需要去探究老板在想啥，应该由PM提前跟老板确认好需求，再跟我们开发沟通好，我们直接按照提供的需求单去开发，最后PM根据需求单去验收，这个是正常的流程。但是现在的情况是，PM不清楚老板的需求，跟老板沟通没到位，然后给我们的需求单也是细节不清晰或者有缺漏的（而且往往是我们开发到一半，细细捋一遍逻辑时才发现不对劲），反而要我们提醒PM后，她才会去跟老板确认细节，然后跟我们反馈完，我们又发现哪里的逻辑有漏洞，再去跟PM提，PM又去问老板，回来再告诉我们这个逻辑漏洞怎么解决——周而复始，反反复复，相当让人心累。所以在之前的博客里说这个项目的沟通成本巨高，有点后悔接了这份工作，但当时的我还不知道，这还不是最坑的……

在四月中旬的时候，我正在忙搬家的事情，然后老板突然说要暂缓开发，因为巴拉巴拉的原因，等巴拉巴拉后就可以继续开发了。我和同事就说，挺好，刚好休息一下，最近真的忙飞了。我就没管了，先是要折腾搬家，然后又要准备去伦敦旅游的事，根本没空啊！直到在伦敦旅游的时候，收到老板的信息说，「巴拉巴拉（一些铺垫），剩下的钱等重启开发后再按月发放，可好？」，才意识到老板是不想付钱了。。。我整个人都无语住了，然后我赶紧算已经收到的钱，只收到了40%！！！我们就跟老板说至少得发到60%才行，后续开发就当新项目重新谈，老板各种推脱说不行啊，现在进度不符合董事预期巴拉巴拉，一堆借口。我其实在这个时候就有预感，这笔钱应该是拿不到了。

不幸的万幸是，本人的拖延症让我没有一次性就把所有工作做完（。）比如说这个平台里有个很核心的功能是生成xxx文档，免去之前每份材料都要手动填写的烦恼，刚开始PM提供的是A模板，后来又说A模板不行，要换成B模板。我觉得这个修改很简单，但有点琐碎，就搁置了它，先去做别的事情去了。现在老板很生气地质问我们：这个修改模板的事情，之前问PM说是已经做好了，现在一看怎么还是旧模板？不用新模板，平台生成的材料就用不了！笑死我了，你这不活该吗，谁叫你不付钱！还有其他一些说大不大，说小也不小的问题，于是这个平台就处于几乎不能用的状态，硬要用也会用着相当难受，老板想让我们先把这些问题给改了，但是他不给钱我们怎么可能改！！没把他们之前那个做好的项目数据库删了就不错了……

这也是做外包很容易遇见的问题吧，但是我们似乎严格来说不算外包？因为一般外包团队中会有专门的PM角色去沟通需求，而我们是一个纯开发团队，感觉我们这几个程序员，就很好骗啊……也没有产品设计和需求协调的主导权。之前我朋友自己组了个外包团队，接过一段时间单，但是后面没有再做了。我去问他原因的时候，他说，一是因为外面行情差，接单难也价格低；二是就算能接到单，钱也不好拿，他已经两年没搞了但现在还有项目款没拿回来。听得我是心有戚戚焉……我之前比较缺钱，而且这个老板和我同事是熟人关系，于是在我同事询问我要不要加入时，我还是爽快答应了。第一个项目合作得还算顺利吧，当时PM还没有这么离谱，给的也足够多，钱也按时打了。于是在他们来找我说要做第二个项目时，我虽然有点犹豫（钱变少了，但是据说需求比之前简单很多），但也答应了。后来回想一下，我觉得这次项目有几个雷：

薪酬没有达到我的预期。工作量大约是前一个项目的60%，但是薪酬只有前一个项目的30%多一点点。我觉得我真的不太擅长估算工作量，如果是一个很具体的需求，我可以估算得比较准，但如果是一整个产品，一个大的功能模块，我就估不准了，所以我前期也没能很好地估算出这个钱和工作量值不值得接……
合同与第一次不一样。第一次与他们合作的时候，我们的合同是采用阶段交付的形式，有详细写分阶段交付的内容，也提到了每个阶段他们应该付的款项，以及违约条款也很明确。这一次签合同时，老板说想把付款方式改成月付款，每个月打一次钱，打半年（用的是什么税相关的借口，鄙人对这个不太了解所以记不得了啊），虽然项目预期是只需要三个月，我寻思着按照之前的经验可能四个月甚至五个月才能彻底做完，那六个月内付清也行吧，我就答应了。后来发现修改付款方式真的是雷啊，从阶段性付改成月付，想不付钱就这么轻松地不付钱了（…
我对同事的信任度太高了。这两次开发项目都是我同事作为沟通的主导角色，去跟老板商量合同或者钱款事宜等等，因为她跟老板是熟人，加上她的人情世故能力比我好太多（本人堪称职场情商低谷），另外我也很认可我同事的工作能力，我们是同一个学校出来的，之前一起共事两年，信任度直接拉满！我就完全信赖她去处理所有事情了，再加上之前一次项目很顺利，因此我都没有仔细检查合同条款就让她帮我签了（不要学我555），直到后面老板拒绝给钱时我才想起，嗯，我还没看过合同呢……大雷中的大雷啊！
合同中的开发计划表形同虚设。一般这种外包合同会附一张开发计划表，但是实际情况由于各种原因很大概率并不会按照计划表进行，那么如果违约了，很难去判断是谁的责任——比如在这个例子中，PM总是改需求，没法提前就给我们一个很详细的东西，那么我们肯定是认为这个拖延责任是在PM，但是一般合同里不会定义「需求交付时间」和「需求确认时间」，而往往会定义「功能验收时间」，那么这其中的延期责任就很难划分。
现在的情况就是老板不想给剩下的钱， 但是他也用不了这个平台，双输啊！项目估计就这么烂尾了。不过呢，之前那个项目服务器也到期了（一年了嘛），证书也到期了，备案也要重新弄，老板就抓瞎了，完全不会弄。他本来还想让自己公司的员工接受帮忙搞，但是那个员工死活搞不定（？）最后就给我们单独付了续费和备案的钱。

我其实已经把这件事情放下了，要不是为了写博客，我也不会啰里八嗦讲这么老多，大家可以由此一窥外包团队的职业危机（？）感觉不抱希望能把钱要回来，但如果他愿意补齐钱款、重新签合同，那也不是不能把剩下的东西给他弄好，但是要是再有新项目，我觉得我不会再参加了。

## 2. 搬家

虽然之前的房子只住了半年，但是由于种种原因，今年大概二月中的时候我就开始看新房子了，一个月左右就找到了新房并签了合同，效率相当高（请夸我找房小能手！）

今年四月份我们一直在忙搬家的事。十分不凑巧的是，我们一月那会儿就订好了四月去伦敦的机酒，两件事就这么撞一起了……所以四月份时真的忙得我焦头烂额，首先是要整理打包搬家的物品，然后是把不需要的物品出二手，最后是给旧房子大扫除；在把所有东西搬到新房子后还要逛二手市场买齐家具，一些大件家具，比如沙发、床、餐桌椅和衣柜等，必须要在搬家当天租了搬家卡车时一起搬到新家去#@¥%&，不用我多说大家都能懂我有多累！！！

这次要搬的新家我其实很满意，户型方方正正，面积比我人生里住过的任何一个住处都大！但它没有任何家具，甚至都没有灯，我们为了给新家买灯还踩了好几个坑——我们没搞清楚这个房子只能装带挂钩的灯，不能往天花板上打孔，买错了灯，现在烂在手里根本出不掉🚬

但没有家具这个事情反而激起了我的装修（？）热情！！！我平时最爱看网上的什么装修小视频、roomtour小视频了！虽然户型不能改，但是软装可以好好整一整嘛！我为了新家绞尽
