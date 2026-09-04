---
title: 安装
date: 2026-09-02
series: ["Tensorflow 学习教程"]
series_order: 2
---


cp3.14 安装报错，使用uv 创建 python 其他版本
```bash
uv python list
uv python pin 3.12
```

uv 安装
```bash
uv init Tensorflow
uv run main.py
uv pip install tensorflow
```

uv 换源
```bash
uv pip install xxx --index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

安装成功后，测试
```bash
python
import tensorflow as tf
Yu = tf.constent(["Hi", "Yuoek"])
print(Yu)
print(Yu.numpy())
```

