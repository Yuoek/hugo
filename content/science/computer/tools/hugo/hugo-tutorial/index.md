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

