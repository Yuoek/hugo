---
title: 开始
date: 2026-09-03
description: "Typescript 教程"
categories: ["Program", "TypeScript"]
series: ["Typescript 学习记录"]
series_order: 2
---

## 安装

使用 nodejs 的 npm 安装，如果没有装 nodejs，Linux 可以使用包管理器安装，以 Ubuntu 为例：

```bash
sudo apt install nodejs
```

使用 npm 安装 typescript

```bash
npm install -g typescript typescript-language-server
```


## 示例

新建 test.ts

```bash
nvim test.ts
```

写入

```ts
var test:string = "Dear Yuoek";
console.log("test");
```

编译
```bash
tsc test.ts
```

运行
```bash
node test.js
```

## 关键字

break       as          any         switch  
case        if          throw       else
var         number      string      get
module      type        instanceof	typeof
public      private     enum        export
finally     for         while       void
null        super       this        new
in          return      true        false
any         extends     static      let
package     implements	interface	function
new	        try	        yield	    const
continue	do	        catch

## ts 与 js 不同点

js
```js
function funSum(a, b) {
    sum = a + b;
    return sum;
}

console.log(funSum(3, 5));
```

ts
```ts
function funSum(a:number, b:number):number {
    sum = a + b;
    return sum;
}

console.log(funSum(3, 5))
```

通过对比发现，typescript 会带有变量类型。

接口 interface
```ts
interface Name {
    firstName: string;
    lastName: string;
    getFullName(): string;
}

let obj: Name = {
    firstName: "Yu",
    lastName: "oek",
    getFullName(): string {
        return this.fistName + " " + this.lastName;
    }
};

console.log(obj.getFullName());
```

类 class
```ts
class DoSome {
    name: string;
    constructor(message: string) {
        this.name = message;
    }

    do() {
        return this.name + "在图书馆学习" ;
    }
}

let doSome = new DoSome("Yuoek");
console.log(doSome.do());
```

继承 inheritance

```ts
class Person {
    name: string;
    constructor(name: string) {
        this.name = name;
    }

    display(): void  {
        console.log(this.name);
    }
}

class Yu extends Person {
    yuoek: string;
    constructor(name: string, yuoek: string) {
        super(name);
        this.yuoek = yuoek;
    }

    do(): string {
        return this.name + "正在" + this.yuoek;
    }
}

let yu = new Yu("Yuoek", "学习 TypeScript");
console.log(yu.do());
```
