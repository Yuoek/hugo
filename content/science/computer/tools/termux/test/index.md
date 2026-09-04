---
title: 安装配置（测试版）
date: 2026-08-26
description: "Termux 教程"
categories: ["Tools", "Termux"]
---


<!-- mtoc-start -->

* [基本配置](#基本配置)
  * [更新](#更新)
  * [换源](#换源)
  * [安装常用软件](#安装常用软件)
  * [获取存储权限](#获取存储权限)
* [zsh 配置](#zsh-配置)
* [neovim 配置](#neovim-配置)
* [图形桌面配置](#图形桌面配置)
  * [proot 容器安装 ubuntu](#proot-容器安装-ubuntu)

<!-- mtoc-end -->

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


### 获取存储权限

```bash
termux-setup-storage
```


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

找到 plugins 并修改为如下然后退出 nvim：
```markdown
plugins=(git zsh-autosuggestions zsh-syntax-highlighting z)
```

安装 starship 主题 [(官网)](https://starship.rs/zh-CN/guide/#%F0%9F%9A%80-installation)
```bash
pkg install starship
```

然后输入：
```bash
echo 'eval "$(starship init zsh)"' >> ~/.zshrc
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

打开 nvim
```bash
nvim
```

等待插件下载完成


## 图形桌面配置

### proot 容器安装 ubuntu
