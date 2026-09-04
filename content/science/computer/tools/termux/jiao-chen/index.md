---
title: 安装配置
date: 2026-08-26
description: "Termux 教程"
categories: ["Tools", "Termux"]
series: ["Termux 学习记录"]
series_order: 1
---


<!-- mtoc-start -->

* [简介](#简介)
* [安装](#安装)
* [基本配置](#基本配置)
  * [更新](#更新)
  * [换源](#换源)
  * [安装常用软件](#安装常用软件)
  * [获取存储权限](#获取存储权限)
  * [修改启动文字](#修改启动文字)
  * [虚拟键盘](#虚拟键盘)
  * [备份解压 (可选)](#备份解压-可选)
* [zsh 配置](#zsh-配置)
* [neovim 配置](#neovim-配置)
* [图形桌面配置](#图形桌面配置)
  * [proot 容器安装 ubuntu](#proot-容器安装-ubuntu)

<!-- mtoc-end -->

## 简介

## 安装

[Termux App 下载：📦 termux-debug_arm64-v8a.apk ](https://ghfile.geekertao.top/https://github.com/termux/termux-app/releases/download/v0.119.0-beta.3/termux-app_v0.119.0-beta.3+apt-android-7-github-debug_arm64-v8a.apk) 

## 基本配置

### 更新

```bash
pkg update && pkg upgrade -y
```

### 换源

```bash
termux-change-repo
```

### 安装常用软件

```bash
pkg install git curl wget zsh vim neovim python clang lldb codelldb
```

**注：** termux 可以使用 pkg 或 apt 管理器进行安装软件

1、可以使用 `apt --help` 进行查看更多命令参数：
| 命令                | 中文说明                                   |
| ------------------- | ------------------------------------------ |
| apt list           | 列出已安装软件包                           |
| apt search         | 按描述搜索软件包                           |
| apt show           | 查看软件包详细信息                         |
| apt install        | 安装软件包                                 |
| apt reinstall      | 重新安装                                   |
| apt remove         | 卸载软件包（保留配置）                     |
| apt autoremove     | 自动卸载不再使用的依赖包                   |
| apt update         | 更新软件源索引（不升级程序）               |
| apt upgrade        | 升级已安装包，不删除旧包                   |
| apt full‑upgrade   | 完整系统升级，必要时会删除旧包             |
| apt edit‑sources   | 编辑软件源配置文件（换源）                 |
| apt satisfy        | 直接满足依赖字符串，一般很少手动用         |


2、或者使用 `pkg` 进行查看：

| 命令 | 中文说明 |
|------|----------|
| pkg autoclean  | 删除 apt 缓存中所有过时软件包 |
| pkg clean  | 清空全部 apt 软件包缓存 |
| pkg files <packages>  | 查看该包安装生成的全部文件 |
| pkg install <packages>  | 安装指定软件包 |
| pkg list‑all  | 列出源中全部可获取软件包 |
| pkg list‑installed  | 列出本机已安装软件包 |
| pkg reinstall <packages>  | 将已安装包重新安装至最新版本 |
| pkg search <query>  | 根据名称、描述关键词搜索软件包 |
| pkg show <packages>  | 查看包元信息，包括依赖关系 |
| pkg uninstall <packages>  | 卸载软件包，保留配置文件 |
| pkg upgrade  | 将已安装包升级到最新版本 |
| pkg update  | 从软件源更新 apt 本地数据库 |

### 获取存储权限

```bash
termux-setup-storage
```

### 修改启动文字

```bash
nvim $PREFIX/etc/motd
```

### 虚拟键盘

```bash
nvim ~/.termux/termux.properties
```

修改如下：

```markdown
extra-keys = []	
```

### 备份解压 (可选)

压缩：

```bash
tar -zcvf /sdcard/v0.10_termux_archlinux.tar.gz -C /data/data/com.termux/files ./home ./usr
```

其中 v0.10_termux_archlinux.tar.gz 为压缩文件名

解压：

```bash
tar -zxvf /sdcard/v0.10_termux_archlinux.tar.gz -C /data/data/com.termux/files --recursive-unlink --preserve-permissions
```

其中 v0.10_termux_archlinux.tar.gz 为要解缩的文件名


## zsh 配置

下载 zsh
```bash
pkg install zsh
```

修改默认 shell
```bash
chsh -s $PREFIX/bin/zsh
```

安装 [oh-my-zsh](https://ohmyz.sh/#install)
```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

下载插件-自动补全和高亮 [(其它插件)](https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins)
```bash
git clone https://gitee.com/asddfdf/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

git clone https://gitee.com/chenweizhen/zsh-autosuggestions.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

修改 .zshrc
首先打开 .zshrc
```bash
nvim ~/.zshrc
```

将 plugins 修改为如下：
```markdown
plugins=(git zsh-autosuggestions zsh-syntax-highlighting z)
```

安装 starship 主题 [(官网)](https://starship.rs/zh-CN/guide/#%F0%9F%9A%80-installation)
```bash
pkg install starship
```

在 ~/.zsh 最后添加以下内容：
```bash
eval "$(starship init zsh)"
```

**重启 termux 后生效**

## neovim 配置

安装 neovim
```bash
pkg install neovim
```

安装 NvChad 配置
```bash
git clone https://github.com/yuoek/starter ~/.config/nvim && nvim
```


## 图形桌面配置

### proot 容器安装 ubuntu
