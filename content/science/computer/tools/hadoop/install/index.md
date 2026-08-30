---
title: 安装配置
date: 2026-08-30
description: "Hadoop 教程"
categories: ["Tools", "Hadoop"]
series: ["Hadoop 学习记录"]
series_order: 1
---


<!-- mtoc-start -->

* [简介](#简介)
* [安装](#安装)

<!-- mtoc-end -->

## 简介

## 安装

使用 Termux Proot-distro 容器 ubuntu-24.04 版本进行安装

切换 root (`su`)后更新
```bash
apt update && apt upgrade
```

jdk 版本查看并切换
```bash

update-alternatives --list java
```

```bash
update-alternatives --config java
```

创建新用户
```bash
useradd -m hadoop
passwd hadoop
```

切换 hadoop 用户并输入密码
```bash
su - hadoop
```

下载 hadoop 二进制包(aarch64)
```bash
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.5.0/hadoop-3.5.0-aarch64.tar.gz
```

解压并移动
```bash
tar -zxvf hadoop-3.5.0-aarch64.tar.gz
mv hadoop-3.5.0-aarch64 ~/hadoop
```

配置环境变量
```bash
export HADOOP_HOME=$HOME/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-arm64
```

添加环境变量到 hadoop-env.sh
```bash
echo "export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-arm64" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh
```

配置 ssh 免密
```bash
ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys
```

测试免密登录
```bash
ssh localhost
```

hadoop 配置

打开 core-site.xml 
```bash
nvim $HADOOP_HOME/etc/hadoop/core-site.xml
```

写入
```xml
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
    <property>
        <name>hadoop.tmp.dir</name>
        <value>file:///home/hadoop/hadoop‑tmp</value>
    </property>
</configuration>
```

打开 hdfs‑site.xml
```bash
nvim $HADOOP_HOME/etc/hadoop/hdfs-site.xml
```

写入
```xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>
```

打开 mapred‑site.xml
```bash
nvim $HADOOP_HOME/etc/hadoop/mapred-site.xml
```

写入
```xml
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<configuration>
    <property>
        <name>yarn.app.mapreduce.am.env</name>
        <value>HADOOP_MAPRED_HOME=/home/hadoop/hadoop</value>
    </property>
    <property>
        <name>mapreduce.map.env</name>
        <value>HADOOP_MAPRED_HOME=/home/hadoop/hadoop</value>
    </property>
    <property>
        <name>mapreduce.reduce.env</name>
        <value>HADOOP_MAPRED_HOME=/home/hadoop/hadoop</value>
    </property>
</configuration>
```

打开 yarn-site.xml
```bash
nvim $HADOOP_HOME/etc/hadoop/yarn-site.xml
```

写入
```bash
<configuration>
    <property>
        <name>yarn.nodemanager.aux‑services</name>
        <value>mapreduce_shuffle</value>
    </property>
</configuration>
```

格式化 hdfs
```bash
hdfs namenode -format
```

启动集群(Termux ssh 22 端口报错)
```bash
start‑all.sh
# 查看进程
jps

# 停止集群
stop‑all.sh
```

使用下面启动
```bash
hdfs --daemon start namenode
hdfs --daemon start datanode
hdfs --daemon start secondarynamenode
yarn --daemon start resourcemanager
yarn --daemon start nodemanager
```

使用下面关闭
```bash
hdfs --daemon stop namenode
hdfs --daemon stop datanode
hdfs --daemon stop secondarynamenode
yarn --daemon stop resourcemanager
yarn --daemon stop nodemanager
```

在浏览器打开 8088 和 9870 端口
```bash
http://localhost:9870
http://localhost:8088
```


