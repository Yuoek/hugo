---
title: "C"
date: 2026-05-09T19:24:39+08:00
mermaid: true
description: ""
categories: ["Code", "Note", "C"]
tags: ["Note","Code", "C"]
series: ["C"]
series_order: 1
type: "posts"
---

这是一个关于 C 语言学习的教程系列，在这里，对 C 语言又进行重新的学习，学它的基本语法结构以及它的高级用法。再用 C 语言实现一些小项目，并且分析一些大型项目的代码，例如 Neovim、Mariadb、Linux等等项目。

# C
## example
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>

// ===================== 1. 宏定义、预处理、常量 =====================
#define PI 3.1415926
#define MAX_LEN 100
#define SQR(x) ((x)*(x))   // 带参宏

// 枚举类型
enum Color {
    RED,
    GREEN,
    BLUE = 10
};

// 类型别名
typedef int DataType;
typedef unsigned char uchar;

// 结构体 + 位域
struct BitData {
    unsigned int a : 2;
    unsigned int b : 3;
    unsigned int c : 1;
};

// 联合体
union UnDemo {
    int num;
    char ch;
    float f;
};

// 普通结构体、结构体嵌套
struct Student {
    char name[20];
    int age;
    float score;
    struct BitData bit;   // 结构体嵌套
};

// 函数声明
void funcBase();
int add(int a, int b);
void swap(int *x, int *y);
void recursive(int n);
void varArg(int count, ...);
void funPtrTest();

// 全局变量
int global_num = 100;

// 函数指针
void showMsg() {
    printf("函数指针被调用\n");
}

int main()
{
    // ===================== 2. 基础数据类型、变量、const =====================
    char ch = 'A';
    short s = 10;
    int i = 20;
    long l = 123456;
    float f = 3.14f;
    double d = 6.28;
    unsigned int ui = 99;
    const int NUM = 88;   // 只读常量

    printf("基础类型：%c %hd %d %ld %.2f %.2lf %u %d\n", ch, s, i, l, f, d, ui, NUM);

    // ===================== 3. 运算符 =====================
    int a = 5, b = 2;
    printf("算术：%d %d %d %.1f %d %d %d\n", 
           a+b, a-b, a*b, (float)a/b, a%b, a++, --b);
    printf("逻辑：%d %d %d\n", 1&&0, 1||0, !1);
    printf("位运算：%d %d %d\n", a&b, a|b, a^b);
    printf("三目：%s\n", a>b ? "a大" : "b大");

    // ===================== 4. 分支语句 if else / switch =====================
    int score = 75;
    if (score >= 90) {
        printf("优秀\n");
    } else if (score >= 60) {
        printf("及格\n");
    } else {
        printf("不及格\n");
    }

    enum Color c = GREEN;
    switch(c) {
        case RED: printf("红色\n"); break;
        case GREEN: printf("绿色\n"); break;
        case BLUE: printf("蓝色\n"); break;
        default: printf("未知颜色\n");
    }

    // ===================== 5. 循环 for / while / do-while / break / continue =====================
    int k;
    for(k = 0; k < 3; k++) {
        if (k == 1) continue;
        printf("for 循环：%d\n", k);
    }

    k = 0;
    while(k < 2) {
        printf("while 循环：%d\n", k);
        k++;
    }

    k = 0;
    do {
        printf("do-while 循环：%d\n", k);
        k++;
    } while(k < 2);

    // ===================== 6. goto 跳转 =====================
    goto endTag;
    printf("这句不会执行\n");
endTag:
    printf("goto 跳转到此处\n");

    // ===================== 7. 数组、字符串 =====================
    int arr[5] = {1,2,3,4,5};
    char str1[] = "C语言语法";
    char str2[20];
    strcpy(str2, "字符串复制");

    printf("数组第2个元素：%d\n", arr[1]);
    printf("字符串：%s %s\n", str1, str2);

    // 二维数组
    int arr2[2][3] = {{1,2,3},{4,5,6}};
    printf("二维数组：%d\n", arr2[1][1]);

    // ===================== 8. 指针、指针变量、指针操作 =====================
    int m = 10;
    int *p = &m;
    printf("变量地址：%p 指针取值：%d\n", &m, *p);

    // 指针数组
    char *strArr[] = {"Java", "C", "Python"};
    printf("指针数组：%s\n", strArr[1]);

    // 数组指针
    int (*pArr)[3] = &arr2[0];
    printf("数组指针取值：%d\n", (*pArr)[0]);

    // ===================== 9. 结构体、联合体、位域 =====================
    struct Student stu = {"小明", 19, 92.5, {1,2,0}};
    printf("结构体学生：%s %d %.2f\n", stu.name, stu.age, stu.score);

    union UnDemo un;
    un.num = 65;
    printf("联合体：%d %c\n", un.num, un.ch);

    // ===================== 10. static 静态变量、全局变量 =====================
    funcBase();
    funcBase();  // 验证static只初始化一次
    printf("全局变量：%d\n", global_num);

    // ===================== 11. 函数调用、递归、指针传参 =====================
    printf("add 结果：%d\n", add(3,7));
    int x1=10, y1=20;
    swap(&x1, &y1);
    printf("交换后：%d %d\n", x1, y1);

    printf("递归输出：");
    recursive(3);

    // 可变参数
    varArg(3, 10,20,30);

    // 函数指针
    void (*fp)() = showMsg;
    fp();

    // ===================== 12. 动态内存分配 =====================
    int *pMem = (int *)malloc(4 * sizeof(int));
    if (pMem != NULL) {
        pMem[0] = 100;
        pMem[1] = 200;
        printf("动态内存：%d %d\n", pMem[0], pMem[1]);
    }
    free(pMem);

    // ===================== 13. 宏使用 =====================
    printf("宏平方：%d\n", SQR(5));

    return 0;
}

// 普通函数 + static局部变量
void funcBase()
{
    static int cnt = 0;  // 静态局部变量
    cnt++;
    printf("static 计数：%d\n", cnt);
}

// 普通求和函数
int add(int a, int b)
{
    return a + b;
}

// 指针做函数参数
void swap(int *x, int *y)
{
    int t = *x;
    *x = *y;
    *y = t;
}

// 递归函数
void recursive(int n)
{
    if (n <= 0) return;
    printf("%d ", n);
    recursive(n-1);
}

// 可变参数函数
void varArg(int count, ...)
{
    va_list ap;
    va_start(ap, count);
    printf("可变参数：");
    for(int i=0; i<count; i++) {
        printf("%d ", va_arg(ap, int));
    }
    va_end(ap);
    printf("\n");
}

```

关于 C 语言的学习，我们先从它的基本语法开始。首先是头文件的引用，引用头文件之后，我们可以在顶部定义一些宏定义、常量等等。接下来从 main 函数主程序入口，然后是变量类型。变量有整型、浮点型、有符号、无符号等等。int、float、double、long long。又学习条件控制语句，if else、if else、for 循环、while 循环、do while 循环。还有 switch，多条件分支选择。在进行选择或循环的时候，有关键字 continue 和 break，特别注意下 continue 和 break 的不同用法。接下来是数组、字符串，字符串和字符的一些区别和联系。学完前面这些作为铺垫，将要学习一种新的数据，就是结构体。与结构体相关的还有联合体、枚举这些。当学完这些对数据的声明、定义、类型，还有一些程序逻辑时，我们可以将每个程序要实现的功能，打包成一块块，把它放在函数里面。对于函数有函数的一些格式参数。哦，对了，还有一个特别重要的概念，就是指针。函数在引用一般的变量名或者数组或者指针的时候，这些参数是如何进行传递的？以及是如何进行返回的？



最近了解到了 Vibe Coding，所以我觉得沉浸式编程是一个很不错的概念，因为我们的大脑和身体不再局限于坐姿和手全排放在键盘上进行代码的敲写，我们可以随时随地以不同的姿势使用我们的语言，让 AI 输入法能更清楚地将我们的想法识别成文字，然后再进行 AI 代码生成，我们再根据这些生成进行反复的修正、测试以及再次迭代，以完成我们最初想要实现的功能。我觉得 Vibe Coding 是不错，但是也有一些局限。比如 AI 怎么才能知道你大脑里面想要实现的是什么功能？你要怎么表达才能更清楚？这里我觉得应该采用分而治之的思想，将我们大脑全局的功能分成一小小块。我们再通过一小小块的提示词给 AI，让 AI 分别实现好之后，我们再来将这些小块拼接成一个整体。就像在软件工程里面学到的单元测试，到集成测试、最终是确认测试。所以我们要做的就是把我们的想法通过切分之后，一一进行描述，让 AI 产生相应的功能。我们既是目标项目的生产者，我们也是目标项目的修改者。


明天是母亲节，要不是今天 Sophiw 发花朵的照片给我看，后面还写着母亲节快乐，我自己都忘了。上次去浙江，还记得很清楚，5 月 10 号是母亲节。但是今天忙碌一天下来，都忘记明天是母亲节了，还在想着明天怎么完成论文作业。哎，忙碌冲昏了头脑，每天麻木的不知道忙些什么。













