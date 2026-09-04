---
title: 示例
date: 2026-09-01
---


<!-- mtoc-start -->

* [mvn](#mvn)
  * [一些命令](#一些命令)
  * [pom.xml](#pomxml)
* [spring-cli](#spring-cli)
* [html ](#html-)

<!-- mtoc-end -->

## mvn

### 一些命令
```bash
mvn clean
mvn spring-boot:run
```

### pom.xml
```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         https://maven.apache.org/xsd/maven-4.0.0.xsd">

    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>4.1.0</version>
        <relativePath/>
    </parent>

    <groupId>com.demo</groupId>
    <artifactId>hello</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>hello</name>

    <properties>
        <java.version>17</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-devtools</artifactId>
            <scope>runtime</scope>
            <optional>true</optional>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>4.1.0</version>
            </plugin>
        </plugins>
    </build>

</project>
```

## spring-cli

默认生成 Gradle
```bash
spring init --dependencies=web hello
```

运行
```bash
./gradlew bootRun
```

生成 maven 项目并构建
```bash
spring init --build=maven --dependencies=web example
cd example
ls
mvn spring-boot:run
```

打开 http://localhost:8080 运行成功

保存自动部署，在 pom.xml <dependencies>...</dependencies> 内加入
```bash
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-devtools</artifactId>
    <scope>runtime</scope>
    <optional>true</optional>
</dependency>
```

## html 

方式一：在入口函数写
```java
@GetMapping("/")
public String index(){
    return "<html><body><h2>首页</h2></body></html>";
}
```

方式二：在 resources/static/index.html 写
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>首页</title>
</head>
<body>
    <h1>Dear: Yuoek</h1>
    <p>遇光见影，遇你见爱。</p>
</body>
</html>
```

`删掉 @GetMapping 方法 和注释 @RestController 有取消注释使得检测到更改自动部署`

