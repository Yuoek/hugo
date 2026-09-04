---
title: dap 配置
date: 2026-08-31
series: ["Nvim 教程"]
series_order: 3
---

<!-- mtoc-start -->

* [tree-sitter-cli ](#tree-sitter-cli-)
* [python](#python)
* [c/cpp](#ccpp)
* [java](#java)
* [go](#go)

<!-- mtoc-end -->


## tree-sitter-cli 

ubuntu
```bash
sudo apt install rustup
rustup default stable
```

使用 cargo 安装 tree-sitter-cli
```bash
cargo install --locked tree-sitter-cli
```

`注： nvim 使用 TSInstall 安装不成功`
[tree-sitter-cli](https://github.com/tree-sitter/tree-sitter/blob/master/crates/cli/README.md)

## python

debugpy
```bash
pip install debugpy
```

uv 安装
```bash
uv pip install debugpy
```

## c/cpp

gcc/gdb
```bash
sudo apt install gcc gdb
```

termux 使用 lldb
```bash
pkg install codelldb lldb
```

## java

lazy.nvim
```lua
{
  'nvim-java/nvim-java',
  config = function()
    require('java').setup()
    vim.lsp.enable('jdtls')
  end,
}
```

## go

`注：dap go 配置失败 😢，就用 python c cpp java 吧，不要再折腾了，写代码才是硬道理！`

golang 安装
```bash
sudo apt install golang
```

go 换源
```bash
go env -w GOPROXY="https://mirrors.aliyun.com/goproxy/,direct"
go env | grep GOPROXY
```

delve 安装(最新版)
```bash
go install github.com/go‑delve/delve/cmd/dlv@latest
```

v1.24
```bash
go install github.com/go-delve/delve/cmd/dlv@v1.24.1
```

dlv 写入环境变量
```bash
echo 'export PATH="$HOME/go/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```
