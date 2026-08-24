---
title: Codex 教程
date: 2026-08-22
---

## Termux 安装

### npm 安装

[npm 安装链接：https://www.npmjs.com/package/@mmmbuto/codex-cli-termux](https://www.npmjs.com/package/@mmmbuto/codex-cli-termux) 

```bash
pkg update && pkg upgrade -y
pkg install nodejs-lts -y
npm install -g @mmmbuto/codex-cli-termux@latest
codex --version
codex 

```

### DeepSeek 注册获取 Api

[DeepSeek Api 链接：https://platform.deepseek.com/usage](https://platform.deepseek.com/usage)

充值获取 api

点击 API Key，创建获取 api key 并复制。

### 使用 DeepSeek 模型脚本

[deepseek 接入链接：https://api-docs.deepseek.com/zh-cn/quick_start/agent_integrations/codex/](https://api-docs.deepseek.com/zh-cn/quick_start/agent_integrations/codex/)

```bash
bash <(curl -fsSL https://cdn.deepseek.com/api-docs/codex-deepseek-setup.sh)
```
