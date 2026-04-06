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


