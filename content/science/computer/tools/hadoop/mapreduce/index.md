---
title: MapReduce
date: 2026-08-30
description: "Hadoop 教程"
categories: ["Tools", "Hadoop"]
series: ["Hadoop 学习记录"]
series_order: 3
---


<!-- mtoc-start -->

<!-- mtoc-end -->

在 Linux hadoop 用户下新建一个测试目录并写入三个文档
```bash
mkdir -p ~/test/hadoop && cd ~/test/hadoop
```

打开 test.txt
```bash
nvim text.txt
```

写入
```txt
hello world
hello hadoop
hello spark
```
打开 mapper.py
```bash
nvim mapper.py
```

写入
```python
#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for w in words:
        print(f"{w}\t1")
```

打开 reducer.py
```bash
nvim reducer.py
```

写入
```python
#!/usr/bin/env python3
import sys

current_word = None
count_sum = 0

for line in sys.stdin:
    line = line.strip()
    word, cnt = line.split("\t")
    cnt = int(cnt)

    if current_word == word:
        count_sum += cnt
    else:
        if current_word is not None:
            print(f"{current_word}\t{count_sum}")
        current_word = word
        count_sum = cnt

# 输出最后一组
if current_word is not None:
    print(f"{current_word}\t{count_sum}")
```

赋予权限并本地测试
```bash
chmod +x mapper.py reducer.py
cat test.txt | ./mapper.py | sort | ./reducer.py
```

创建目录
```bash
hdfs dfs -mkdir -p /user/hadoop/mr/input
```

上传目录
```bash
hddfs dfs -put test.txt /user/hadoop/mr/input
```

提交 mapreduce 任务
```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-files mapper.py,reducer.py \
-mapper mapper.py \
-reducer reducer.py \
-input /user/hadoop/mr/input/* \
-output /user/hadoop/mr/output
```

查看 hdfs 输出结果
```bash
hdfs dfs -cat /user/hadoop/mr/output/part-00000
```

删除输出目录
```bash
hdfs dfs -rm -r -skipTrash /user/hadoop/mr/output
```
