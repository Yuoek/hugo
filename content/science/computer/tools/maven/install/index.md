---
title: Maven 安装
date: 2026-08-31
series: ["Maven 教程"]
series_order: 1
---

<!-- mtoc-start -->

* [安装](#安装)

<!-- mtoc-end -->


## 安装

ubuntu
```bash
sudo apt install maven
```

spring boot 创建项目
```bash
curl https://start.spring.io/starter.zip \
  -d dependencies=web \
  -d type=maven-project \
  -d baseDir=spring-app \
  -o spring-app.zip
unzip spring-app.zip
cd spring-app
```
