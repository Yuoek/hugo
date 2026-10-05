---
title: install
date: 2026-09-24
---

## jdk 安装

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install openjdk

# 验证
java -version
javac -version
```

## tomcat 下载

```bash
# 下载tomcat9
wget https://archive.apache.org/dist/tomcat/tomcat-9/v9.0.85/bin/apache-tomcat-9.0.85.tar.gz

# 解压到/usr/local
sudo tar -zxvf apache-tomcat-9.0.85.tar.gz -C /usr/local/
cd /usr/local
sudo mv apache-tomcat-9.0.85 tomcat9

# 给脚本执行权限
sudo chmod +x /usr/local/tomcat9/bin/*.sh
```

## maven 安装

```bash
sudo apt update
sudo apt install maven -y
# 校验
mvn -v
```

## 目录创建

maven 创建 web 项目
```bash
# 生成webapp骨架项目
mvn archetype:generate \
-DgroupId=com.demo \
-DartifactId=servlet-demo \
-DarchetypeArtifactId=maven-archetype-webapp \
-DinteractiveMode=false
```


进入项目目录
```bash
cd servlet-demo
```

修改 pom.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.demo</groupId>
    <artifactId>servlet-demo</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>war</packaging>

    <properties>
        <maven.compiler.source>8</maven.compiler.source>
        <maven.compiler.target>8</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
            <version>4.0.1</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <finalName>servlet-demo</finalName>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <version>3.3.2</version>
            </plugin>
        </plugins>
    </build>
</project>
```

在 src/main/java/com/demo/HelloServlet.java 写入
```java
package com.demo;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

public class HelloServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        resp.setContentType("text/html;charset=utf-8");
        PrintWriter out = resp.getWriter();
        out.println("<h1>Maven Servlet 运行成功！</h1>");
    }
}

```

在 src/main/webapp/WEB-INF/web.xml 写入
```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">

    <servlet>
        <servlet-name>hello</servlet-name>
        <servlet-class>com.demo.HelloServlet</servlet-class>
    </servlet>
    <servlet-mapping>
        <servlet-name>hello</servlet-name>
        <url-pattern>/hello</url-pattern>
    </servlet-mapping>
</web-app>

```

maven 打包生成 war
```bash
# 清理旧构建 + 打包
mvn clean package
```

tomcat 部署
```bash
# 将war复制到tomcat webapps目录
sudo cp target/servlet-demo.war  ~/apache-tomcat-9.0.122/webapps/
```
