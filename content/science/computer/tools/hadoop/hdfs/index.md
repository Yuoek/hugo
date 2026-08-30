---
title: HDFS
date: 2026-08-30
description: "Hadoop 教程"
categories: ["Tools", "Hadoop"]
series: ["Hadoop 学习记录"]
series_order: 2
---


<!-- mtoc-start -->

* [简介](#简介)
* [HDFS 常用命令](#hdfs-常用命令)

<!-- mtoc-end -->

## 简介

![hdfs](https://www.tutorialspoint.com/hadoop/images/hdfs_architecture.jpg) 

## HDFS 常用命令


| Linux本机(ubuntu磁盘) | HDFS命令(`hdfs dfs`) | 功能说明 |
|---|---|---|
| ls | hdfs dfs -ls | 列出目录 |
| ls -R | hdfs dfs -ls -R | 递归列出所有子目录 |
| mkdir | hdfs dfs -mkdir | 创建文件夹 |
| mkdir -p a/b/c | hdfs dfs -mkdir -p /a/b/c | 递归创建多级目录 |
| cat file | hdfs dfs -cat /xxx/file | 输出文件全部内容 |
| head -n10 file | hdfs dfs -head /xxx/file | 查看文件头部 |
| tail -n10 file | hdfs dfs -tail /xxx/file | 查看文件尾部 |
| cp src dst | hdfs dfs -cp src dst | HDFS内部复制 |
| mv src dst | hdfs dfs -mv src dst | HDFS内部移动/重命名 |
| rm file | hdfs dfs -rm /xxx/file | 删除文件 |
| rm -r dir | hdfs dfs -rm -r /xxx/dir | 递归删除目录 |
| rm -rf dir | hdfs dfs -rm -r -skipTrash /xxx/dir | 直接删除，跳过回收站 |
| du -h | hdfs dfs -du -h | 查看目录、文件占用大小 |
| df -h | hdfs dfs -df -h | 查看HDFS磁盘整体使用情况 |
| chmod 755 file | hdfs dfs -chmod 755 /xxx/file | 修改文件权限 |
| chown user:group file | hdfs dfs -chown hadoop:hadoop /xxx/file | 修改文件属主 |
| find ./ -name "*.txt" | hdfs dfs -find /user/hadoop -name "*.txt" | 在HDFS查找文件 |
| touch file | hdfs dfs -touchz /user/hadoop/test.txt | 创建空文件 |
| wc -l file | hdfs dfs -cat /xxx/file \| wc -l | 统计文件行数 |
| — | hdfs dfs -put 本地路径 HDFS路径 | **本地上传到HDFS** |
| — | hdfs dfs -get HDFS路径 本地路径 | **从HDFS下载到本机** |
| — | hdfs dfs -copyFromLocal 本地 HDFS | 等同于put，上传 |
| — | hdfs dfs -copyToLocal HDFS 本地 | 等同于get，下载 |
| — | hdfs dfs -appendToFile 本地文件 /hdfs/file | 将本地文件内容追加到HDFS文件末尾 |


