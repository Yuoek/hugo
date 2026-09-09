---
title: 开始
date: 2026-09-03
description: "PHP 教程"
categories: ["Program", "PHP"]
series: ["PHP 学习记录"]
series_order: 2
---

## 安装

ubuntu 安装
```bash
sudo apt install php-fpm php-mysql nginx
```

termux(proot-distro) 配置 nginx 端口为 8080
```bash
nano /etc/nginx/sites-available/default
```

启动
```bash
sudo /etc/init.d/php8.3-fmp start
sudo /etc/init.d/nginx start
```

启动成功，浏览器打开
```bash
http://localhost:8080
```
