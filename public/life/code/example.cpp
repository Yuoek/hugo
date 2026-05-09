
#include <iostream>
#include <iostream>
#include <vector>
#include <string>
#include <memory>
#include <thread>
#include <stdexcept>

// ===================== 1. 命名空间、预处理、宏、别名 =====================
#define MAX_NUM 100
using namespace std;

namespace MyNS {
    void show() { cout << "自定义命名空间\n"; }
}

typedef long long ll;
using Str = string;

// 枚举、强类型枚举
enum Color { RED, GREEN, BLUE };
enum class Week : int { MON = 1, TUE };

// ===================== 2. 基础类型、auto、constexpr、引用 =====================
constexpr double PI = 3.1415926;

// 全局变量
int g_val = 999;

// ===================== 3. 函数重载、内联函数、默认参数 =====================
inline int square(int x) { return x * x; }
int add(int a, int b);
double add(double a, double b);   // 函数重载
void funcDefault(int a = 10, int b = 20);

// ===================== 4. 类、封装、访问控制、构造析构 =====================
class Person {
private:
    // 私有成员
    string name;
    int age;
    static int count;          // 静态成员变量
    const int id;              // 常量成员

public:
    // 构造函数
    Person();
    Person(string n, int a, int i);
    // 拷贝构造
    Person(const Person& p);
    // 移动构造
    Person(Person&& p) noexcept;
    // 析构
    ~Person();

    // 成员函数、const成员函数
    void setInfo(string n, int a);
    void showInfo() const;

    // 静态成员函数
    static void showCount();

    // 友元函数
    friend void friendFunc(Person& p);
};

// 静态成员初始化
int Person::count = 0;

// 构造析构实现
Person::Person() : id(1001) {
    name = "未知"; age = 0;
    count++;
}
Person::Person(string n, int a, int i) : id(i) {
    name = n; age = a;
    count++;
}
Person::Person(const Person& p) : id(p.id) {
    name = p.name; age = p.age;
    count++;
    cout << "拷贝构造调用\n";
}
Person::Person(Person&& p) noexcept : id(p.id) {
    name = move(p.name);
    age = p.age;
    count++;
    cout << "移动构造调用\n";
}
Person::~Person() {
    count--;
    cout << "析构函数调用\n";
}

void Person::setInfo(string n, int a) {
    name = n;
    age = a;
}
void Person::showInfo() const {
    cout << "姓名:" << name << " 年龄:" << age << " 编号:" << id << endl;
}
void Person::showCount() {
    cout << "当前对象数:" << count << endl;
}

// 友元函数
void friendFunc(Person& p) {
    cout << "友元访问私有姓名:" << p.name << endl;
}

// ===================== 5. 继承、多继承、虚继承、多态、抽象类 =====================
// 抽象类(含纯虚函数)
class Animal {
public:
    virtual void speak() = 0;   // 纯虚函数
    virtual ~Animal() = default;
};

// 公有继承
class Dog : public Animal {
public:
    virtual void speak() override;  // 重写
};
void Dog::speak() {
    cout << "小狗汪汪叫\n";
}

// 虚继承
class BaseA { public: int x; };
class BaseB : virtual public BaseA {};
class BaseC : virtual public BaseA {};
class Derive : public BaseB, public BaseC {};

// ===================== 6. 运算符重载 =====================
class Point {
public:
    int x, y;
    Point(int a = 0, int b = 0) : x(a), y(b) {}
    // 重载+
    Point operator+(const Point& p) const {
        return Point(x + p.x, y + p.y);
    }
    // 重载<< 全局友元
    friend ostream& operator<<(ostream& os, const Point& p);
};
ostream& operator<<(ostream& os, const Point& p) {
    os << "(" << p.x << "," << p.y << ")";
    return os;
}

// ===================== 7. 模板：函数模板、类模板 =====================
template <typename T>
T maxVal(T a, T b) {
    return a > b ? a : b;
}

template <class T>
class TemplateDemo {
private:
    T val;
public:
    TemplateDemo(T v) : val(v) {}
    T getVal() { return val; }
};

// ===================== 8. 异常处理 try-throw-catch =====================
void throwDemo() {
    throw runtime_error("手动抛出运行时异常");
}

// ===================== 9. Lambda 表达式 =====================
void lambdaDemo() {
    auto add = [](int a, int b) { return a + b; };
    cout << "Lambda结果:" << add(3,5) << endl;

    int x = 10;
    auto inc = [&x](){ x++; };
    inc();
    cout << "Lambda捕获引用 x=" << x << endl;
}

// ===================== 10. STL 容器、范围for =====================
void stlDemo() {
    vector<int> vec = {1,2,3,4};
    for(auto v : vec) {  // 范围for
        cout << v << " ";
    }
    cout << endl;
}

// ===================== 11. 智能指针 =====================
void smartPtrDemo() {
    unique_ptr<string> up = make_unique<string>("unique_ptr测试");
    shared_ptr<int> sp1 = make_shared<int>(666);
    shared_ptr<int> sp2 = sp1;
    cout << "智能指针值:" << *sp1 << endl;
}

// ===================== 12. 类型转换 =====================
void castDemo() {
    int a = 10;
    double b = static_cast<double>(a);
    int* p = &a;
    char* cp = reinterpret_cast<char*>(p);
    cout << "类型转换:" << b << endl;
}

// ===================== 13. 多线程 =====================
void threadFunc() {
    cout << "子线程运行\n";
}

// 普通函数实现
int add(int a, int b) { return a + b; }
double add(double a, double b) { return a + b; }
void funcDefault(int a, int b) {
    cout << "默认参数 a=" << a << " b=" << b << endl;
}

// ===================== main 主函数 =====================
int main() {
    // 基础语法
    int a = 10;
    double b = 3.14;
    auto c = "auto推导字符串";
    int& ref_a = a;   // 引用
    ref_a = 20;
    cout << "引用修改后a=" << a << endl;

    // 命名空间
    MyNS::show();

    // 函数重载、默认参数
    cout << "add int:" << add(1,2) << " add double:" << add(1.5,2.5) << endl;
    funcDefault();

    // 类与对象
    Person p1;
    Person p2("张三", 20, 2001);
    p2.showInfo();
    Person p3 = p2;        // 拷贝构造
    Person p4 = move(p2);  // 移动构造
    Person::showCount();
    friendFunc(p3);

    // 多态、抽象类
    Animal* ani = new Dog();
    ani->speak();
    delete ani;

    // 运算符重载
    Point pt1(1,2), pt2(3,4);
    Point pt3 = pt1 + pt2;
    cout << "运算符重载:" << pt3 << endl;

    // 模板
    cout << "模板max:" << maxVal(5,9) << endl;
    TemplateDemo<int> tpl(100);
    cout << "类模板值:" << tpl.getVal() << endl;

    // 异常处理
    try {
        throwDemo();
    } catch (exception& e) {
        cout << "捕获异常:" << e.what() << endl;
    }

    // Lambda
    lambdaDemo();

    // STL
    stlDemo();

    // 智能指针
    smartPtrDemo();

    // 类型转换
    castDemo();

    // 多线程
    thread t(threadFunc);
    t.join();

    // 枚举
    cout << "普通枚举:" << GREEN << endl;
    cout << "强枚举:" << (int)Week::MON << endl;

    return 0;
}
#include <vector>
#include <string>
#include <memory>
#include <thread>
#include <stdexcept>

// ===================== 1. 命名空间、预处理、宏、别名 =====================
#define MAX_NUM 100
using namespace std;

namespace MyNS {
    void show() { cout << "自定义命名空间\n"; }
}

typedef long long ll;
using Str = string;

// 枚举、强类型枚举
enum Color { RED, GREEN, BLUE };
enum class Week : int { MON = 1, TUE };

// ===================== 2. 基础类型、auto、constexpr、引用 =====================
constexpr double PI = 3.1415926;

// 全局变量
int g_val = 999;

// ===================== 3. 函数重载、内联函数、默认参数 =====================
inline int square(int x) { return x * x; }
int add(int a, int b);
double add(double a, double b);   // 函数重载
void funcDefault(int a = 10, int b = 20);

// ===================== 4. 类、封装、访问控制、构造析构 =====================
class Person {
private:
    // 私有成员
    string name;
    int age;
    static int count;          // 静态成员变量
    const int id;              // 常量成员

public:
    // 构造函数
    Person();
    Person(string n, int a, int i);
    // 拷贝构造
    Person(const Person& p);
    // 移动构造
    Person(Person&& p) noexcept;
    // 析构
    ~Person();

    // 成员函数、const成员函数
    void setInfo(string n, int a);
    void showInfo() const;

    // 静态成员函数
    static void showCount();

    // 友元函数
    friend void friendFunc(Person& p);
};

// 静态成员初始化
int Person::count = 0;

// 构造析构实现
Person::Person() : id(1001) {
    name = "未知"; age = 0;
    count++;
}
Person::Person(string n, int a, int i) : id(i) {
    name = n; age = a;
    count++;
}
Person::Person(const Person& p) : id(p.id) {
    name = p.name; age = p.age;
    count++;
    cout << "拷贝构造调用\n";
}
Person::Person(Person&& p) noexcept : id(p.id) {
    name = move(p.name);
    age = p.age;
    count++;
    cout << "移动构造调用\n";
}
Person::~Person() {
    count--;
    cout << "析构函数调用\n";
}

void Person::setInfo(string n, int a) {
    name = n;
    age = a;
}
void Person::showInfo() const {
    cout << "姓名:" << name << " 年龄:" << age << " 编号:" << id << endl;
}
void Person::showCount() {
    cout << "当前对象数:" << count << endl;
}

// 友元函数
void friendFunc(Person& p) {
    cout << "友元访问私有姓名:" << p.name << endl;
}

// ===================== 5. 继承、多继承、虚继承、多态、抽象类 =====================
// 抽象类(含纯虚函数)
class Animal {
public:
    virtual void speak() = 0;   // 纯虚函数
    virtual ~Animal() = default;
};

// 公有继承
class Dog : public Animal {
public:
    virtual void speak() override;  // 重写
};
void Dog::speak() {
    cout << "小狗汪汪叫\n";
}

// 虚继承
class BaseA { public: int x; };
class BaseB : virtual public BaseA {};
class BaseC : virtual public BaseA {};
class Derive : public BaseB, public BaseC {};

// ===================== 6. 运算符重载 =====================
class Point {
public:
    int x, y;
    Point(int a = 0, int b = 0) : x(a), y(b) {}
    // 重载+
    Point operator+(const Point& p) const {
        return Point(x + p.x, y + p.y);
    }
    // 重载<< 全局友元
    friend ostream& operator<<(ostream& os, const Point& p);
};
ostream& operator<<(ostream& os, const Point& p) {
    os << "(" << p.x << "," << p.y << ")";
    return os;
}

// ===================== 7. 模板：函数模板、类模板 =====================
template <typename T>
T maxVal(T a, T b) {
    return a > b ? a : b;
}

template <class T>
class TemplateDemo {
private:
    T val;
public:
    TemplateDemo(T v) : val(v) {}
    T getVal() { return val; }
};

// ===================== 8. 异常处理 try-throw-catch =====================
void throwDemo() {
    throw runtime_error("手动抛出运行时异常");
}

// ===================== 9. Lambda 表达式 =====================
void lambdaDemo() {
    auto add = [](int a, int b) { return a + b; };
    cout << "Lambda结果:" << add(3,5) << endl;

    int x = 10;
    auto inc = [&x](){ x++; };
    inc();
    cout << "Lambda捕获引用 x=" << x << endl;
}

// ===================== 10. STL 容器、范围for =====================
void stlDemo() {
    vector<int> vec = {1,2,3,4};
    for(auto v : vec) {  // 范围for
        cout << v << " ";
    }
    cout << endl;
}

// ===================== 11. 智能指针 =====================
void smartPtrDemo() {
    unique_ptr<string> up = make_unique<string>("unique_ptr测试");
    shared_ptr<int> sp1 = make_shared<int>(666);
    shared_ptr<int> sp2 = sp1;
    cout << "智能指针值:" << *sp1 << endl;
}

// ===================== 12. 类型转换 =====================
void castDemo() {
    int a = 10;
    double b = static_cast<double>(a);
    int* p = &a;
    char* cp = reinterpret_cast<char*>(p);
    cout << "类型转换:" << b << endl;
}

// ===================== 13. 多线程 =====================
void threadFunc() {
    cout << "子线程运行\n";
}

// 普通函数实现
int add(int a, int b) { return a + b; }
double add(double a, double b) { return a + b; }
void funcDefault(int a, int b) {
    cout << "默认参数 a=" << a << " b=" << b << endl;
}

// ===================== main 主函数 =====================
int main() {
    // 基础语法
    int a = 10;
    double b = 3.14;
    auto c = "auto推导字符串";
    int& ref_a = a;   // 引用
    ref_a = 20;
    cout << "引用修改后a=" << a << endl;

    // 命名空间
    MyNS::show();

    // 函数重载、默认参数
    cout << "add int:" << add(1,2) << " add double:" << add(1.5,2.5) << endl;
    funcDefault();

    // 类与对象
    Person p1;
    Person p2("张三", 20, 2001);
    p2.showInfo();
    Person p3 = p2;        // 拷贝构造
    Person p4 = move(p2);  // 移动构造
    Person::showCount();
    friendFunc(p3);

    // 多态、抽象类
    Animal* ani = new Dog();
    ani->speak();
    delete ani;

    // 运算符重载
    Point pt1(1,2), pt2(3,4);
    Point pt3 = pt1 + pt2;
    cout << "运算符重载:" << pt3 << endl;

    // 模板
    cout << "模板max:" << maxVal(5,9) << endl;
    TemplateDemo<int> tpl(100);
    cout << "类模板值:" << tpl.getVal() << endl;

    // 异常处理
    try {
        throwDemo();
    } catch (exception& e) {
        cout << "捕获异常:" << e.what() << endl;
    }

    // Lambda
    lambdaDemo();

    // STL
    stlDemo();

    // 智能指针
    smartPtrDemo();

    // 类型转换
    castDemo();

    // 多线程
    thread t(threadFunc);
    t.join();

    // 枚举
    cout << "普通枚举:" << GREEN << endl;
    cout << "强枚举:" << (int)Week::MON << endl;

    return 0;
}
