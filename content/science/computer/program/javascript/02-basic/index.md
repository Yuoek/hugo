---
title: 基础
date: 2026-09-03
description: "Javascript 教程"
categories: ["Program", "JavaScript"]
series: ["Javascript 学习记录"]
series_order: 3
---


<!-- mtoc-start -->

* [变量](#变量)
  * [变量类型](#变量类型)
* [输出](#输出)
  * [alert()](#alert)
  * [document.write()](#documentwrite)
  * [console.log()](#consolelog)
  * [innerHTML](#innerhtml)
* [注释](#注释)
* [作用域](#作用域)
* [数据类型](#数据类型)
  * [类型转换](#类型转换)

<!-- mtoc-end -->

## 变量

var
```js
var a = 1;
var s = "Yuoek";
```

let
```js
let c = 1;
c = 5;
```

const
```js
const PI = 3.14159;
```

区别
var：全局变量，不在 {} 内，可以先使用再声明定义
let: 局部变量，变量可以修改
const：静态变量，赋值后不可以修改

### 变量类型

数字
```js
var num = 10;
```

字符串
```js
var str = "String";
```

布尔
```js
var b = true;
```

命名
```js
var _name1 = "Name1";
var $name2 = "Name2";
```


##  输出

### alert()
```js
alert("Hello, Yuoek");
```

### document.write()
```js
document.write("Hello, Yuoek");
```

### console.log()
```js
console.log("Hello, Yuoek");
```
示例
```js
  <script>
    console.log("Happy Everyday!")
    var num1 = 10;
    var num2 = 20;
    console.log("The Sum is: " + num1 + num2)
    var obj = {
      id: "2557",
      name: "Yuoek",
      age: "25"
    };
    console.log(obj);
    let message = "Do you best";
    console.log(message);
  </script>
```

### innerHTML
```js
<div id="Yu"></div>

<script>document.getElementById("Yu").innerHTML = "JavaScript Tutorial"</script>
```

## 注释

单行
```js
// 这是注释
```

多行
```js
/*
这也是注释
*/
```



## 作用域

```js
var num = "这是全局变量";
function life() {
    var num = "这是局部变量";
    document.write(num);
}
```

let 同名变量在函数外不生效
```js
  <script>
    let x = 10;
    var y = 20;
    function vl() {
      let x = 100;
      var y = 200;
      document.write("x: " + x + "<br>" + "y: " + y);
    }
    vl();
  </script>
```

修改变量
```js
var a = 10;
var a = 100;
```

赋值，使用后再声明
```js
a = 50;
document.write("a 是：" + a);
var a;
```

静态变量
```js
const b;
b = 100;
// 只能赋值一次，下面报错
b = 200;
```

使用块作用域
```js
{
    const b = "Yuoek";
}
const b = "Sophie";
```

静态数组
```js
const arr = ["Javascript", "c", "python"];
const[0] = "haskell";
arr.push("html");
document.write(arr);
```

静态对象
```js
const cobj{
    name: "Yuoek";
    age: "18";
};
cobj.name = "Sophie";
cobj.age = "17";
document.write(JSON.stringify(cobj));
```

不先使用再声明
```js
document.write(x);
const x = 10;
```

| Comparison basis | var | let | const |
| -------------- | ---- | --- | ------ |
| Scope      | Function |  Block  | Block |
| Hoisted    | Yes   |	No  | No  |
| Reassign   | Yes   |  Yes |   No |
| Re-declare |  Yes  | 	No  | No  |
| Bind This  | Yes   | No   | No  |


## 数据类型

string
```js
var s1 = "这是字符串1";
var s2 = '这是字符串2';
var s3 = `这是字符串3`;
```

numbers
```js
var n1 = 12e8;
var n2 = 20e-8;
```

boolean
```js
var b = true;
var c = false;
```

null
```js
var ty;
var name = "Name";
var name = null;
```

undefined
```js
var ty;
var name = "Name";
var name = undefined;
```


BigInt
```js
let BigNum = 1535837495935037423925305n;
```

Symbol
```js
let syb1 = Symbol("520");
let syb2 = Symbol("520");
let same == syb1 == syb2
```


Object
```js
let name = "Yuoek";
const obj = {
    age: 18;
    name: name;
};
```

Array
```js
const arr = ["c", "cpp", "python", "java", "html", "css", "javascript"];
```

Date
```js
let date = new date();
```

动态类型
```js
let d = 'Yuoe';
d = 18;
d = true;
```

typeof
```js
let name = "yuoek";
let age = 18;
document.write(typeof name + "<br>")
document.write(typeof age + "<br>")
```

### 类型转换

转字符串
```js
document.write("10" + 20 + "<br>");
document.write("10" + true + "<br>");
document.write("10" + null + "<br>");
document.write("10" + undefined + "<br>");

// String()
document.write(typeof String(10))

// toString()
const num = 100;
num.toString()
```

转数字
```js
document.write(("10" + 20) + "<br>");
document.write(("10" + true) + "<br>");
document.write(("10" + null) + "<br>");
document.write(("10" + undefined) + "<br>");

// num
document.write(Number('100'));
document.write(Number(null));
document.write(Number(false));
```


转布尔
```js
num = !!0;
num = !! 1;
str = !!"";
str = !!"Hello";


document.write(Boolean("100"));
document.write(Boolean(null));
document.write(Boolean(undefined));
```

date 转 字符串和数字
```js
// to Number
Number(date);
// or
date.getTime();

// to String
String(date);
// or 
date.toString();
```


Value	String conversion	Number conversion	Boolean conversion
0	    "0"             	0               	false
1   	"1"             	1               	true
"1" 	"1"             	1               	true
"0" 	"0"             	0               	true
""  	""              	0               	false
"Hello"	"Hello"         	NaN             	true
true	"true"	            1                   true
false	"false"	            0                   false
null	"null"	            0                   false
undefined	"undefined"	    NaN                 false
[50]	"50"	            50                  true
[50, 100]	"[50, 100]"	    NaN                 true

