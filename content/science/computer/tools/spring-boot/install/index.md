---
title: 安装
date: 2026-09-01
---

## sprint cli 安装

sdk 安装
```bash
curl -s "https://get.sdkman.io" | bash
```


写入 .zshrc
```bash
source "$HOME/.sdkman/bin/sdkman-init.sh"

echo 'source "$HOME/.sdkman/bin/sdkman-init.sh"' >> ~/.zshrc
```

验证
```bash
sdk version
```

sdk 安装 java-17
```bash
sdk install java 17.0.13-tem
```

使用
```bash
sdk use java 17.0.13‑tem
```

设为默认
```bash
sdk default java 17.0.13‑tem
```

安装 springboot
```bash
sdk install springboot
```

验证
```bash
spring --version
```

查看 springboot
```bash
sdk ls springboot
```


