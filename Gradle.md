```

```

# 一、 Gradle和Groovy的引入

## 1.1 本课程适合的人群

从事Android相关的开发人员
从事Java相关的开发人员
有项目构建基础的人群

## 1.2 为什么要学习Gradle

* 一款最新的，功能最强大的构建工具，用它逼格更高
* 使用Groovy或Kotlin代替XML，使用程序代替传统的XML配置，项目构建更灵活
* 丰富的第三方插件，让你随心所欲使用
* 完善Android,Java开发技术体系

## 1.3 DSL与GPL

DSL 其实是 Domain Specific Language 的缩写，中文翻译为领域特定语言（下简称 DSL）；而与 DSL 相对的就是 GPL，是General Purpose Language 的简称，即通用编程语言，也就是我们非常熟悉的Java、Python 以及 C 语言等等。

## 1.4 Groovy的引入

Groovy是一种JVM语言，它可以编译为与Java相同的字节码，然后将字节码文件交给JVM去执行，并且可以与Java类无缝地互操作，Groovy可以透明地与Java库和代码交互，可以使用Java所有的库。
Groovy也可以直接将源文件解释执行。
它还极大地清理了Java中许多冗长的代码格式。
如果你是Java程序员，那么学习Groovy简直毫无压力。
Groovy尚未成为主流的开发语言，但是它已经在测试（由于其简化的语法和元编程功能）和构建系统中占据了一席之地。
即支持面向对象编程也支持面向过程编程，即可以作为编程语言也可以作为脚本语言

# 二、环境搭建

## 2.1 JDK的安装

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/15c476307ef049e59f69e7c0b96c621f.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/9cc90300ac324561bf76a30cae59596d.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/c621deb55d654151806948280639f6a0.png)

## 2.2 JDK的卸载

控制面板卸载即可

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/96e49970aa60418bb3cec17fd495bdd0.png)

## 2.3 验证JDK是否安装成功

通过控制命令台查看：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/f22ec27bdfe04e3788f7fe57a46b2ce7.png)

## 2.4 下载groovy-sdk

下载地址：https://groovy.apache.org/download.html

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/082d24de53944a8cb3bb1c42a813d8ab.png)

点击下载：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/70f03c866b24453caeea3124ffadd5db.png)

版本搭配：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/03e2cf1af1ca4b81bd6649d5f2368925.png)

## 2.5 groovy-sdk目录结构

将apache-groovy-sdk-3.0.9.zip解压到合适的位置即可，主要目录结构就是bin和doc:

bin目录：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/e83ef39e33644a6f831d4082884b28f2.png)

doc目录：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/f4b73296db44445f8b649eae6ae17c08.png)

## 2.6 配置Groovy环境变量

GROOVY_HOME的配置，值为刚才解压的路径：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/bae3ac3550624fee94d48b099015d01c.png)

Path的配置，借助GROOVY_HOME：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/eea183cdecfb4126b25753de2f940cca.png)

在控制台中输入groovy -version，较验是否正确安装：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/d7ff3e7143c24c349ea095b5e6c86d0a.png)

## 2.7 IntelliJ IDEA的下载和安装

IDEA 全称IntelliJ IDEA，是用于java语言开发的集成环境IDE(Integrated Development Environment)，也可用于其他语言。IntelliJ在业界被公认为最好的java开发工具之一，尤其在智能代码助手、代码自动提示、重构、J2EE支持、Ant、JUnit、CVS整合、代码审查、 创新的GUI设计等方面的功能可以说是超常的。

官网：https://www.jetbrains.com/idea/download/#section=windows

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/3079269528614d10bdfc9a4d8aa4f37a.png)

**安装的准备：**
（1）硬件环境：
内存8G以上
CPU i5以上
安装在固态硬盘下
（2）软件环境：
需要安装JDK

**IDEA的安装：**

首先进入欢迎安装界面，点击“next”即可：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/5dac711c38c24120acf1ee9d6947a979.png)

选择IDEA的安装路径，点击“next”继续：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/71ba7643fcc9422586a0e7542398252e.png)

选择适合安装在64位操作系统上的IDEA，点击“next”继续：（我使用机器为64位系统）

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/4d21881e243341bd899918fdda804b49.png)

选择开始菜单中IDEA的文件夹名字，可以自定义，但是一般用默认的JetBrains即可，点击“next”开始安装：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/913b76a3315741248554b9c40b2510ad.png)

显示安装进度，等待即可：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/19980e46445d4c2d964084d45b22d9dd.png)

安装好以后，选择 `Run IntelliJ IDEA Community Edition`，即可启动IDEA：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/82667b3d14354c1faeb69d13fd904268.png)

进入IDEA后，首先要接收相关协议：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/82e68160897345749a909ccb2e52cf40.png)

接收协议后，点击Continue，进入到IDEA首页：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/4572710a55c94c04b06c1403488eceb5.png)

可以看到IDEA默认的主题效果是暗黑色调的，我们可以将主题调节为明亮色调：选择 `Customize`，在Color theme中选择 `IntelliJ Light`主题，主题颜色立马切换为明亮色调：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/8474f6a1de25490c83affbcca9ee4023.png)

## 2.8 创建Groovy工程并编写第一段程序

（1）创建项目：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/4fccee5c03af4d2f8f857676e86e3af2.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/49d93fe9cb424181a339b9edb8c37708.png)

（2）新建类：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/e0b9062c887a4faebb8633eebd1c5b63.png)

运行结果：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/9dcf04d70fc44f338a252281cc5f60ef.png)

精简语法：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/ba81770924334ea299fcdcacbc8225ea.png)

再次精简：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/19dc3cd04fac478382d95ab663446625.png)

# 三、Groovy语法讲解

## 3.1 变量的类型

在Groovy中，没有基本数据类型，只有对象类型，表面上我们定义基本数据类型，但实际都会帮我们装箱处理：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/bde87ba7dd8f4b438e8592938d48efe2.png)

无论定义基本数据类型还是对象类型，其实都会帮我们转为对象类型

但是对于程序员来说，写代码没有影响

## 3.2 变量的定义

**（1）强类型定义方式**

数据类型  变量名  = 初始值

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/47df8b5089ee4e1b9f869b20b0ee9a9e.png)
**（2）弱类型定义方式**
根据值可以推断出变量的数据类型，所以类型不用显示声明，直接用def即可

def  变量名  = 初始值

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/a0dd42261ddf4d449bfa7ba266d21cde.png)

用def这种弱类型定义可以随便改变类型。

如果不希望别人改变数据类型，用强类型

如果是你自己使用，并且想要随意更改类型，那么就用弱类型

## 3.3 字符串

### 3.3.1 字符串的常用定义方式

**（1）单引号定义方式**

**（2）双引号定义方式**

**（3）三引号定义方式**

```
package com.msb.test01

//单引号形式定义字符串：等价于Java中双引号的定义方式：
def str1 = 'hi groo\nvy1'
println str1
println str1.class //class java.lang.String

//双引号形式定义字符串：
def str2 = "hi groovy2"
println str2
println str2.class //class java.lang.String

//三引号形式定义字符串：
def str3 = '''hi groovy3'''
println str3
println str3.class  //class java.lang.String

//三种方式区别在哪里：
//用单引号形式定义字符串，那么字符串的格式需要自己去控制，比如加：转义字符
//用三引号的形式，我们可以直接在字符串中定义格式：
//如果想要写的形式和展示形式一样，可以在第一个三引号后加入\
def str4 = '''\
hi
groovy4'''
println str4

//双引号形式的字符串：可扩展字符串：
def str5 = "groovy5"
def str6 = "hi ${str5}"  //拼接变量
println str6 //hi groovy5
println str6.class //class org.codehaus.groovy.runtime.GStringImpl

//拼接表达式：可扩展表达式融入到字符串中去
def str7 = "100 + 100 = ${100 + 100}"
println str7
println str7.class


//总结：双引号形式定义用的最多 - 因为可扩展特性

//String和GString使用的时候不用互相转化：
//验证：
def str8 = test(str6)//GString类型作为实参传入test方法中，返回String类型
println str8
println str8.class
//定义方法：
String test(String s){
    return s
}

```

### 3.3.2 字符串的常用方法

**（1）可直接使用java.lang.String中的方法：**

```
package com.msb.test01

def str1 = "higroovy"
println "字符串的长度为：" + str1.length()
println "字符串是否为空：" + str1.isEmpty()
println "获取字符串的下标对应的字符为：" + str1.charAt(2)

def str2 = "higroovy"
println "判断两个字符串是否相等：" + str1.equals(str2)
println "字符串从固定位置截取：" + str1.substring(3)
println "字符串从区间位置截取：" + str1.substring(2,4)
println "替换字符串为新字符串：" + str1.replace('o', 'O')

def str3 = "a-b-c-d-e-f"
def split = str3.split("-")
println "按照指定的字符串进行分裂为数组的形式:" + split

def str4 = "higroovy"
println "转大写字母：" + str4.toUpperCase()
println "转小写字母：" + str4.toUpperCase().toLowerCase()

def str5 = "  hi groovy  "
println "去除收尾空格：" + str5.trim()

def str6 = "a"
def str7 = "b"
println "字符串的比较：" + str6.compareTo(str7)
```

**（2）使用org.codehaus.groovy.runtime.StringGroovyMethods中方法：**

```
package com.msb.test01

def str1 = "higroovy"
println "以str1字符串为中心在两侧用空格进行填充为指定长度：" + str1.center(12)
println "以str1字符串为中心在两侧用字符a进行填充为指定长度：" + str1.center(12,'a')

println "在str1的左侧进行填充：" + str1.padLeft(10,'a')

def str2 = "hellogroovy"
def str3 = "groovy"
println "减法操作：去掉重复内容：" + str2.minus(str3)

def str4 = "higroovy"
println "字符串的逆转/倒叙："+ str4.reverse()

println "首字母大写" + str4.capitalize()

def str5 = "123"
println "类型的转换：" + str5.toInteger().class
```

**（3）Groovy中新增的操作符**

```
//操作符-进行比较
def str6 = "a"
def str7 = "b"
println str6 > str7  //false

//操作符：获取字符串指定下标上的字符：
def str8 = "groovy"
println str8[1]
println str8[2..3] //oo

//操作：减法操作：
def str9 = "hellogroovy"
def str10 = "groovy"
println str9 - str10

```

## 3.4 流程控制

流程控制分为：顺序结构、分支结构、循环结构

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/6337cbe63e6649af9184e700ef5cb402.png)

### 3.4.1 switch-case分支

```
package com.msb.test01

def a = 74
//在Groovy中a可以是任意类型：
switch (a){ //按照类型比较：a.class
    //case后面可以按照不同类型进行判断：
    case 'abc':
        println "这是第1个分支"
        break;
    case [4,7,9]: //列表
        println "这是第2个分支"
        break;
    case 45..98: //范围
        println "这是第3个分支"
        break;
    case Integer:
        println "这是第4个分支"
        break;
    case BigDecimal:
        println "这是第5个分支"
        break;
    default:
        println "这是第6个分支"
        break;
}


```

在switch-case结构中，非常灵活，所以也非常常用

### 3.4.2 for循环

```
package com.msb.test01

//普通循环：
for(def i = 1;i <= 10;i++){
    println i
}
println "----------------------------"
//对范围循环：
for(i in 10..30){
    println i
}
println "----------------------------"
//对列表循环：
for(i in [1,2,3,4,5]){
    println i
}

println "----------------------------"
//对Map循环：
for(i in [1002:"zhangsan",2004:"lisi",9004:"zhuliu"]){
    println i.key + "-----" + i.value
}
```

## 3.5 闭包

### 3.5.1 闭包的基本技能点

**闭包的定义：**

闭包就是一段代码块，用{}括起来：

```
def c = { println 'hi groovy'}
```

**闭包调用/执行：**

```
c.call()
c() //类似调用方法一样
```

**闭包传入参数：**

**无参数**：

```
// -> 前：闭包参数   -> 后：闭包体
def c = { -> println 'hi groovy'}
c.call()
```

**可以传入一个参数**：

```
def c = { String str -> println "hi ${str}"}
c.call('groovy')
```

**可以传入多个参数**：（用逗号隔开参数即可）

```
def c = { String str,int num -> println "hi ${str} , hi ${num}"}
def num = 19
c.call('groovy',num)
```

**有默认的参数：**

所有闭包都有一个默认参数，不需要你显式声明，用it接收

```
def c = { println "hi ${it} "}
c.call('groovy')
```

如果你不想叫it，那么就需要自己手动显式将参数定义即可，一旦定义那么就没有默认参数了（隐式参数）

**闭包返回值：**

闭包一定有返回值，如果不写，就相当于返回null

```
def c = { println "hi ${it} "}
def result = c.call('groovy')
println result
```

可以定义返回值：

```
def c = { return "hi ${it} "}
def result = c.call('groovy')
println result
```

### 3.5.2 闭包的常见使用场景

#### **1、与基本数据类型结合使用（for循环场景）**

（1）案例：从2-7进行遍历： -------**upto**

```
2.upto(7){println it}
```

底层对应源码：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/a0d6ea436fa54db9812d934b8b9f2e4d.png)

（2）案例：1+2+3+。。。。+100   -------**upto**

```
//1+2+3+。。。。+100
def result = 0
1.upto(100){result += it}
println result
```

（3）案例：输出7-2 -------**downto**

```
7.downto(2){println it}
```

（4）案例：输出100以内的数  --- **times**  (从0开始遍历到指定数结束)

```
3.times {println it}
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/97fdde86d060445cb9e72c1dc22f2bec.png)

结果：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/544e0057af75418288d6b217a61f3ed3.png)

（5）案例：1+2+。。。100  ----- **times**

```
def r = 0
101.times {r += it}
println r
```

补充：写法两种：

```
//如果闭包是调用方法的最后一个参数，可以直接将闭包写在外面
2.upto(7){println it} //常用
2.upto(7,{println it}) //不常用
```

#### **2、与字符串结合使用**

```
package com.msb.test01

def s = "hi groovy 2023"

//遍历：PS :如果闭包是方法的最后一个参数，我们可以写在外面，不用非要写到()中
println s.each {println it} //each的返回值就是字符串s本身

//找到符合条件的第一个值
println s.find {it.isNumber()}
//PS :参照源码发现 !bcw.call(new Object[]{value} --》闭包返回值必须是布尔值

//找到符合条件的全部值
def list = s.findAll {it.isNumber()}
println list.toListString()

//判断任意一位是否满足条件
println s.any {it.isNumber()}

//判断每一位是否满足条件
println s.every {it.isNumber()}

//收集结果：
def list2 = s.collect {it.toUpperCase()}
println list2.toListString()
```

### 3.5.3 闭包中的变量

1、this

this代表定义该闭包的类的实例对象（实例闭包）或者类本身（静态闭包）。

2、owner

可以和this用法一样，还可以用作：当闭包中嵌套闭包的时候，这时候owner就指向定义它的闭包对象

3、delegate

它的含义大多数情况下是跟owner的含义一样，除非它被显示的修改

**在Groovy脚本中定义闭包，那么this，owner，delegate指代的都是当前所在的脚本的类的对象（当前脚本编译后对应的就是一个脚本类型的类）**

```
//定义闭包：
def c1 = {
    println "c1-this:" + this
    println "c1-owner:" + owner
    println "c1-delegate:" + delegate
}

//闭包调用：
c1.call()
```

结果：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/1a60c0d220644ab1ab445472a15e41f9.png)

**定义内部类：**

如果定义内部类，那么无论是闭包中还是方法中，this，owner，delegate指代的都是所在类的对象-Person的对象

```
//定义内部类：
class Person{
    //定义闭包：
    def c2 = {
        println "c2-this:" + this
        println "c2-owner:" + owner
        println "c2-delegate:" + delegate
    }

    //定义方法：
    def test(){
        //定义闭包：
        def c3 = {
            println "c3-this:" + this
            println "c3-owner:" + owner
            println "c3-delegate:" + delegate
        }
        //调用闭包：
        c3.call()
    }
}
//定义Person对象:
Person p = new Person()
//调用内部类的闭包：
p.c2.call()
//调用内部类的方法：
p.test()
```

结果：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/2ad5fd49a6d24f8abdea19682267e9e5.png)

如果定义的内容是静态的，那么this，owner，delegate指代的就是所在的类-Person

```
//定义内部类：
class Person{
    //定义闭包：
    def static c2 = {
        println "c2-this:" + this
        println "c2-owner:" + owner
        println "c2-delegate:" + delegate
    }

    //定义方法：
    def static test(){
        //定义闭包：
        def c3 = {
            println "c3-this:" + this
            println "c3-owner:" + owner
            println "c3-delegate:" + delegate
        }
        //调用闭包：
        c3.call()
    }
}
//定义Person对象:
//Person p = new Person()
//调用内部类的闭包：
Person.c2.call()
//调用内部类的方法：
Person.test()
```

**闭包中嵌套闭包：**

this指代的依然是所在的类，但是owner，delegate指代的就是嵌套闭包的闭包

```
//闭包中嵌套闭包：
def c4 = {
    def c5 = {
        println "c5-this:" + this
        println "c5-owner:" + owner
        println "c5-delegate:" + delegate
    }
    c5.call()
}

//闭包的调用：
c4.call()
```

结果：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/2b12eea014924fd0bc73458aa71550cd.png)

**总结1：**

无论什么情况下，this指代的都是所在类/类的对象

但是如果遇到闭包嵌套闭包，owner，delegate指代的就是嵌套闭包的闭包

**owner，delegate不同的情况：它的含义大多数情况下是跟owner的含义一样，除非它被显示的修改**

```
Person p = new Person()
//闭包中嵌套闭包：
def c4 = {
    def c5 = {
        println "c5-this:" + this
        println "c5-owner:" + owner
        println "c5-delegate:" + delegate
    }
    c5.delegate = p
    c5.call()
}

//闭包的调用：
c4.call()
```

结果：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/83566a8b6a4b4484b14d30fb27359b73.png)

**总结2：**

delegate的含义大多数情况下是跟owner的含义一样，除非它被显示的修改

### 3.5.4 闭包委托策略

PS：写脚本用的少，了解即可。

```
package com.msb.test01

//定义A类
class A{
    String name
    def ac = {
        "name = ${name}"
    }
    String toString(){
        ac.call()
    }
}

//定义B类
class B {
    String name
}

//定义对象：
def a = new A(name:"丽丽")
def b = new B(name:"菲菲")
//调用a对象的方法：
println a.toString()


```

结果：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/d0de90bc740d44deb6c0cfd874e6ce9c.png)

原因：

${name}取值是从delegate中取值，所以delegate默认情况下指代的是当前A的对象

想要得到菲菲的结果，解决修改delegate:

```
//定义对象：
def a = new A(name:"丽丽")
def b = new B(name:"菲菲")
//修改delegate
a.ac.delegate = b
//调用a对象的方法：
println a.toString()
```

但是发现修改delegate不好用，因为默认情况下delegate委托机制是owner fisrt,所以我们需要修改委托策略：

```
//定义对象：
def a = new A(name:"丽丽")
def b = new B(name:"菲菲")
//修改delegate
a.ac.delegate = b
a.ac.resolveStrategy = Closure.DELEGATE_FIRST
//调用a对象的方法：
println a.toString()
```

结果：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/109fbe3222cc48159b5c8d5841d55f71.png)

总结：${name}默认从delegate取值，delegate默认和owner的值一样，委托机制也是owner_first优先，所以你光改变delegate的值没用，需要修改委托策略为：delegate_first

## 3.6 列表

#### 3.6.1 列表的定义

```
package com.msb.test01

//定义集合：
def list = new ArrayList() //java中的定义方式：
//groovy中的定义ArrayList的方式：
def list2 = [1,2,3,4,5,6,7]
println list2.class  //class java.util.ArrayList
println list2.size()  //7

//groovy中的定义数组的方式：
def arr = [1,2,3,4] as int[]
int[] arr2 = [1,2,3,4]
println arr.class //class [I
println arr2.class //class [I
```

#### 3.6.2 列表的使用

**添加元素、删除元素：**

```
package com.msb.test01

//定义列表：
def list = [1,2,3,4,5,6]

//添加操作
list.add(7)
println list.toListString()
list.leftShift(8)
println list.toListString()
list << 9
println list.toListString()
def newList = list + 10
println newList.toListString()

//删除操作：
def list2 = [1,2,3,4,5,6]
//按照索引删除操作：
list2.remove(3)
println list2.toListString()
list2.removeAt(0)
println list2.toListString()
//按照指定元素删除：
list2.remove((Object)5)
println list2.toListString()
list2.removeElement(6)
println list2.toListString()
//按照指定条件删除元素：
def list3 = [1,2,3,4,5,6]
list3.removeAll{it % 2 == 0}  //删除所有的偶数
println list3.toListString()

//使用操作符删除：
def list4 = [1,2,3,4,5,6]
def newlist = list4 - [4,5,6]
println newlist


```

**排序操作：**

```
package com.msb.test01

//定义列表：
def list = [-3,-1,4,0,5,2,-6]

//排序操作：
list.sort()  //按照升序排列
println list

//按照指定条件排序：
list.sort{num1,num2 -> num1 == num2 ? 0 : Math.abs(num1) < Math.abs(num2) ? -1 : 1}//按照绝对值的大小排泄液
println list

def strlist = ['a','abcdef','abc','ab']
strlist.sort{return it.size()} //按照字符串的长度排毒
println strlist


```

**查找操作：**

```
package com.msb.test01

//定义列表：
def list = [-3,-1,4,0,5,2,-6]

println list.find{it % 2 == 0}  //找到列表中的第一个偶数
println list.findAll{it % 2 == 0}  //找到列表中的所有偶数

println list.any {it % 2 == 0 } //只要列表中有一个偶数，那么就返回true
println list.every {it % 2 == 0 } //列表中必须每个元素都是偶数的时候，才会返回true

println list.min() //获取最小值
println list.max() //获取最大值

//做统计：
println list.count {return it >= 0  }

```

## 3.7 映射

#### 3.7.1 映射的定义

```
package com.msb.test01

//定义Java中的HashMap
//def hm = new HashMap()

//在Groovy中定义：
def map = ['张三':1001,
           '李四':2003,
           '王五':9006]

println map.toMapString()

//添加元素：通过key添加value
map['朱六'] = 9005
println map.toMapString()
map.'刘七' = 7001
println map.toMapString()
map.'newMap' = ['x':1,'y':2]
println map.toMapString()

//上述代码中，key部分是单引号的不可变字符串，可以单引号省略不写：
def map2 = [张三:1001,
           李四:2003,
           王五:9006]
println map2.toMapString()
//println map2.class //通过.class方式获取map2的类型不可以
println map2.getClass() //在groovy中默认的映射：class java.util.LinkedHashMap类型
def map3 = [张三:1001,
            李四:2003,
            王五:9006] as Hashtable
println map3.getClass()
Hashtable map4 = [张三:1001,
            李四:2003,
            王五:9006]
println map4.getClass()
```

#### 3.7.2 映射的使用

**映射的遍历：**

```
package com.msb.test01

def map = ['张三':1001,
           '李四':2003,
           '王五':9006,
           '朱六':9005,
           'newMap':['x':1,'y':2]]
//进行遍历操作：
map.each{println it.key + "----" + it.value}
map.each{key,value -> println key + "----" + value}

//带索引的遍历：
map.eachWithIndex{ Map.Entry<String, Serializable> entry, int index -> println  entry.key + "----" + entry.value + "-----" + index}
map.eachWithIndex{key,value,index -> println  key + "----" + value + "-----" + index}

```

**映射的查找：**

```
package com.msb.test01

def map = ['张三':['score':68,'sex':'女'],
           '李四':['score':32,'sex':'男'],
           '王五':['score':71,'sex':'女'],
           '朱六':['score':74,'sex':'男']]
//查找：
//找到映射中第一个score大于70的键值对信息：
println map.find{it.value.score > 70}
//找到映射中所有score大于70的键值对信息：
println map.findAll{it.value.score > 70}

println map.count{it.value.score > 60 && it.value.sex == '女'}

//先查询出成绩在70以上的键值对信息，在此基础上或者key的部分：
println map.findAll {it.value.score > 70}
.collect {it.key}
//分组：
println map.groupBy {it.value.score >= 60 ? "及格" : "不及格"}
```

**映射的排序：**

```
package com.msb.test01

def map = ['张三':['score':68,'sex':'女'],
           '李四':['score':32,'sex':'男'],
           '王五':['score':71,'sex':'女'],
           '朱六':['score':74,'sex':'男']]

//排序：
//按照指定的条件进行排序：按照学生的成绩排列：
def newMap = map.sort{def stu1,def stu2 ->
    def score1 = stu1.value.score
    def score2 = stu2.value.score
    return score1 == score2 ? 0 : score1 < score2 ? 1 : -1
}

println newMap


```

## 3.8 范围（Range）

```
package com.msb.test01

//定义一个范围：
//定义范围指的就是定义从2到5的范围：2,3,4,5
def r = 2..5
println r.size()

def r2 = 3..<8  //3,4,5,6,7
println r2.size()

//操作：
println r[1]  //通过索引获取元素
println r.contains(4)  //判断是否包含某个具体的数值
println r2.from //范围开始的数字
println r2.to //范围结束的数字

//通过查看源码，发现Range实际就是List的一种，与列表的操作一致
//有了列表为什么还要用范围？ 轻量级的列表，如果定义连续范围可以使用范围

//遍历：
r.each{println it}

for(ele in r2){
    println ele
}



```

在switch-case中的应用：

```
def a = 74
//在Groovy中a可以是任意类型：
switch (a){ //按照类型比较：a.class
//case后面可以按照不同类型进行判断：
case 'abc':
println "这是第1个分支"
break;
case [4,7,9]: //列表
println "这是第2个分支"
break;
case 45..98: //范围
println "这是第3个分支"
break;
case Integer:
println "这是第4个分支"
break;
case BigDecimal:
println "这是第5个分支"
break;
default:
println "这是第6个分支"
break;
}
```

## 3.9 面向对象

### 3.9.1 类的定义和对象的定义

新建groovy类：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/03333e9ef3a54795885d793c5275ffb1.png)

**类的定义：**

```
package com.msb.test02
//groovy中所有东西默认都是public修饰的
class Student {
    //属性
    String name
    Integer age
    //定义构造器：
//    Student(name,age){
//        this.name = name
//        this.age = age
//    }
}

```

**对象的定义：**

```
package com.msb.test02

//创建对象：
//不用构造器：
//def s1 = new Student()
//println s1
//没有显示定义构造器的时候，我们依然可以在定义对象的时候对属性进行初始化赋值：
def s5 = new Student(name:"丽丽",age:19)
println s5
def s6 = new Student(name:"丽丽")
println s6


//显式编写了构造器，就可以用如下方式使用构造器：
//def s2 = new Student("丽丽",19)
//def s3 = ["娜娜",17] as Student
//Student s4 = ["露露",15]
//println s2
//println s3
//println s4


```

**属性的取值：**

无论是用.的方式直接取值，还是用get/set的方式取值，实际底层调用的都是get/set方法

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/acaab2505c1c440bab273b5c9e2697f4.png)

### 3.9.2 方法的定义和调用

**方法的定义：**

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/2dac108c7961480fb901302301392601.png)

**方法的调用：**

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/5873330a913f4fe39dfd45702c1df113.png)

**方法调用的补充：**

```
package com.msb.test08

//定义方法：
def m1(param){
    println "这是m1方法"
}

//对方法调用：
m1("aa")
m1 "bb"   //调用方法的时候，（）可以省略不写，后面接参数列表即可,如果有多个参数，用逗号拼接参数即可
println "打印一句话"
println("打印一句话")

//定义方法：
def m2(Closure c){
    println "这是m2方法"
}

//调用方法：
m2({String name -> println name})
//如果闭包作为参数的话，闭包可以写在外侧：
m2{String name -> println name}


```

### 3.9.3 接口

**创建接口：**

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/356be167bba544f599c3b29b386d5583.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/0a153099f9bb442099fea795dbaa4ad4.png)

PS :在groovy中不可以定义非public类型的方法

**类中实现接口：**

```
package com.msb.test02
//groovy中所有东西默认都是public修饰的
class Student implements TestInterface{
    //属性
    String name
    Integer age
  

    @Override
    void a() {

    }

    @Override
    def b(Object param1) {
        return null
    }
}

```

### 3.9.4 Trait

用的少，知道即可 。

定义：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/1513ed63e73b4c1b896bc5ba4639d699.png)

```
trait Swiming {
    //抽象方法：abstract修饰符必须加上
    abstract void drink()
    //实现方法：
    def swim(){
        println '可以游泳'
    }
}
```

在Trait中定义抽象方法和非抽象方法，定义以后就可以让类来使用（使用和接口很像，用implements来实现Trait）：

```
class Duck implements Swiming{

    @Override
    void drink() {
        println '游泳的时候喝到水了'
    }
}

```

在脚本中定义具体的对象调用方法：

```
def d = new Duck()
d.drink()
d.swim()
```

运行结果：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/c56509e67118448f918fd1d8cb9113e0.png)

一个类可以实现多个Trait（解决了多继承问题）

```
trait Flying {
    def fly(){
        println '可以飞行'
    }
}
```

```
class Duck implements Swiming,Flying{

    @Override
    void drink() {
        println '游泳的时候喝到水了'
    }
}
```

```
def d = new Duck()
d.drink()
d.swim()
d.fly()
```

结果：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/c7644dc19ad24498b4d3706076a060d7.png)

PS：Trait就像是抽象类和接口的结合，类实现用implements关键字来实现，可以实现多个Trait

### 3.9.5 元编程-方法调用和拦截

使用运行时元编程，我们可以在运行时截取类和接口的方法。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/437f261282234f15ac647cd2e1d4995b.png)

定义一个类：

```
class Person {
    String name
    Integer age

    //方法：
    def eat(){
        return '可以吃饭'
    }
}
```

在脚本中创建对象，调用方法：

```
//定义Person对象：
def p = new Person(name:'丽丽',age:19)
//调用Person中已有的方法直接调用：
println p.eat()

p.play()
```

发现：调用已有的eat方法，直接调用没有问题，但是调用没有的方法play会直接出错：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/f3ebfe57d0db43cbb779125a64556e1e.png)

但是在groovy中可以用重写方法的形式来替换不存在的方法：

```
package com.msb.test03

class Person {
    String name
    Integer age

    //方法：
    def eat(){
        return '可以吃饭'
    }

    @Override
    Object invokeMethod(String name, Object args) {
        println '调用了invokeMethod方法'
        return "当前这个方法是：" + name + ",当前这个方法的参数是：" + args
    }
}

```

```
package com.msb.test03

//定义Person对象：
def p = new Person(name:'丽丽',age:19)
//调用Person中已有的方法直接调用：
println p.eat()

println p.play()
```

结果：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/16fef863ba5a4de5b44d0c95e4150240.png)

如果重写了methodMissing方法，会调用methodMissing方法：

```
package com.msb.test03

class Person {
    String name
    Integer age

    //方法：
    def eat(){
        return '可以吃饭'
    }

    @Override
    Object invokeMethod(String name, Object args) {
        println '调用了invokeMethod方法'
        return "当前这个方法是：" + name + ",当前这个方法的参数是：" + args
    }

    def methodMissing(String name, Object args){
        println '调用了methodMissing方法'
        return "当前这个方法是：" + name + ",当前这个方法的参数是：" + args
    }
}

```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/9d6e0ee8355244308019bf2b8d9bc990.png)

### 3.9.6 元编程-metaClass

使用运行时元编程，我们可以在运行时注入，合成类和接口的方法。

```
package com.msb.test04
//动态为Person类添加sex属性：
Person.metaClass.sex = "女"
//创建Person对象：
def p = new Person(name:"丽丽",age:19)
p.sex = "男"
println p.sex

//动态为Person类添加方法：
Person.metaClass.setNameUpperCase = {->name.toUpperCase()}
def p2 = new Person(name:"abcdef",age:19)
println p2.setNameUpperCase()

////动态为Person类添加静态方法：
Person.metaClass.static.setNameLowerCase = {String name->name.toLowerCase()}
println Person.setNameLowerCase("ABCDEF")
```

## 3.10 Groovy对Json的操作

### 3.10.1 Groovy自带的工具类处理json方式

（1）将对象转为json串：

（2）将json串转为对象：

```
package com.msb.test05

import groovy.json.JsonOutput
import groovy.json.JsonSlurper

//将对象 ---》 Json串：
def p = new Person(name:"lucy",age:19)
println JsonOutput.toJson(p)  // '{"age":19,"name":"lucy"}'

def list = [new Person(name:"lucy",age:19),new Person(name:"lilei",age:21),new Person(name:"lulu",age:17)]
println JsonOutput.toJson(list) //[{"age":19,"name":"lucy"},{"age":21,"name":"lilei"},{"age":17,"name":"lulu"}]

//打印带格式的json串：
def jsonstr = JsonOutput.toJson(list)
println JsonOutput.prettyPrint(jsonstr)
//将Json串---》 对象 :
def str = '{"age":19,"name":"lucy"}'
def js = new JsonSlurper()
def p2 = (Person)(js.parseText(str))
println p2

def list2 = js.parseText('[{"age":19,"name":"lucy"},{"age":21,"name":"lilei"},{"age":17,"name":"lulu"}]')
println list2.class



```

### 3.10.2 使用java第三方类库处理json

将第三方类库导入程序中：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/e8a25dfefd944cf3b58f94749beb0eb1.png)

类：

```
class Person {
    String name
    Integer age
}

```

脚本中转换：

```
package com.msb.test05

import com.google.gson.Gson

//将对象转为json串：
def p = new Person(name:"lili",age:19)

def gson = new Gson()
println gson.toJson(p)   //{"name":"lili","age":19}

//将json串转为对象：
def p2 = gson.fromJson('{"name":"lili","age":19}',Person.class)
println p2

```

## 3.11 Groovy对xml的操作

### 3.11.1 对xml进行解析

```
package com.msb.test05

final String xml = '''
<students>
    <student id="1">
        <name>张三</name>
        <age>18</age>
        <sex>男</sex>
        <score>98</score>
    </student>
    <student id="2">
        <name>李四</name>
        <age>21</age>
        <sex>女</sex>
        <score>93</score>
    </student>
    <student id="3">
        <name>王五</name>
        <age>19</age>
        <sex>女</sex>
        <score>89</score>
    </student>
</students>
'''

//解析xml：
def xs = new XmlSlurper()
def students = xs.parseText(xml)
//获取节点的值：
println students.student[0].name.text()

//获取属性的值：
println students.student[1].@id
```

**xml的遍历：**

```
def list = []
students.student.each{
    it -> list.add(it.name.text() + "---" + it.age.text())
}

println list.toListString()
```

### 3.11.2 生成xml

```
package com.msb.test05

import groovy.xml.MarkupBuilder
def s = new StringWriter()
//生成xml核心类：
def mb = new MarkupBuilder(s)
//创建根节点：看上去像一个方法，但是实际不是方法，只是语法长这样 - 伪方法
//()中传入这个节点的属性 {}中写入这个节点下的节点
mb.students(){
    //第1个student节点：()中传入student节点的属性，{}中传入student下的节点
    student(id:'1'){
        name(a:'a','张三')
        age('18')
        sex('男')
        score('98')
    }

    //第2个student节点：()中传入student节点的属性，{}中传入student下的节点
    student(id:'2'){
        name('李四')
        age(){
            va('21')
        }
        sex('女')
        score('93')
    }
}

println s


```

## 3.12 Groovy对文件的操作

**操作普通文件：**

```
package com.msb.test06

def file = new File("d://students.xml")
file.eachLine {println it}  //it:每行数据
println '-------------------------------'
//获取文件中所有内容：
println file.getText()
println '-------------------------------'
//返回的是一个列表，将每行内容放入列表中
def list = file.readLines()
println list.toListString()
println '-------------------------------'
//读取部分内容
println file.withReader {
    char[] buffer = new char[100]
    it.read(buffer) //读取100个字符的内容
    return buffer
}
println '-------------------------------'
//文件复制：
def copy(String srcPath,String descPath){
    //确定目标文件：
    def descFile = new File(descPath)
    if(!descFile.exists()){//如果目标文件不存在，我们创建目标文件
        descFile.createNewFile()
    }
    //复制：
    new File(srcPath).withReader {
        def lines = it.readLines()
        descFile.withWriter {
            lines.each {line ->
                it.append(line + "\r\n")
            }
        }
    }
    return true
}

println copy("d://students.xml","d://mystudents.xml")
```

**将对象写入文件中：**

```
package com.msb.test07

def saveObject(Object obj,String path){
    //先将文件封装为对象：
    def file = new File(path)
    if(!file.exists()){
        file.createNewFile()
    }
    file.withObjectOutputStream {
        it.writeObject(obj)
    }
    return true
}
def s = new Student(name:"露露",age:18)
saveObject(s,"d://demo.txt")


```

**从文件中将对象读取出来：**

```
def readObject(String path){
    def obj = null //读取的对象
    //创建文件路径对应的文件对象：
    def file = new File(path)
    //判断文件不存在返回null
    if(file == null || !file.exists()){
        return null
    }

    file.withObjectInputStream {
        obj = it.readObject()//读取后给obj赋值
    }
    return obj
}
//调用方法读取
def s2 = (Student)readObject("d://demo.txt")
println s2.name + "---" + s2.age
```

# 四、Gradle的学习

## 4.1 Gradle的优势

* 一款最新的，功能最强大的构建工具，用它逼格更高
* 使用Groovy或Kotlin代替XML，使用程序代替传统的XML配置，项目构建更灵活
* 丰富的第三方插件，让你随心所欲使用
* 完善Android,Java开发技术体系

## 4.2 Gradle的下载和安装

下载位置：https://services.gradle.org/distributions/

PS：下载只有二进制文件的即可（bin那个压缩包）

## 4.3 配置环境变量

配置GRADLE_HOME：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/f9b372f027c54b0684289fc81a29187d.png)

配置Path：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/40ce5422c26146bcbdb7d0b84f4b2cb5.png)

验证Gradle是否安装成功：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/3e0b7dce510644a893e4f772883d26bd.png)

## 4.4 创建第一个Gradle项目

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/0cb1bdd90c9443fd85fd1449a990c4bb.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/5831972b62c24e569993cd753fbcb334.png)

标准项目结构：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/5764784498254a8dbdced837703289f1.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/875b1cd9c642432eb3d548caefe840e6.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/70827e091fd64e3a9d3340f6be9af8a9.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/2f732b4f34994e71b8b1ced8cc9ade48.png)

项目打包：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/9efdc1cfac514b52b5c58fbee2b7dd62.png)

执行：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/2f459dda9ca64a82b11a3f83061c2762.png)

如果出现乱码，在builde.gradle中加入配置：（更改后重新clean再build）

```
plugins {
    id 'java'
}

group 'com.msb'
version '1.0-SNAPSHOT'

repositories {
    mavenCentral()
}

dependencies {
    testImplementation 'org.junit.jupiter:junit-jupiter-api:5.6.0'
    testRuntimeOnly 'org.junit.jupiter:junit-jupiter-engine'
}

test {
    useJUnitPlatform()
}

tasks.withType(JavaCompile) {
    options.encoding = "UTF-8"
}
```

PS:![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/bdbbbea5e6be4411a21f2dd7d2c4b892.png)

## 4.5 build.gradle构建脚本介绍

Gradle构建脚本中最重要的两个概念是project和Task,任何一个Gradle构建都由一个或者多个project组成每个project包括许多的构建部分,可以是一个jar包,也可以是一个web应用,也可以是多个jar的整合,可以部署应用和搭建环境.

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/8eae1fa5b9ed4a0e9ed6c75a1ca0c528.png)

如果有子项目的话：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/dca29235332e4f52bab435b1c10c3ad2.png)

每个项目，对应一个build.gradle的构建脚本

### 4.5.1 Project

一个project代表一个正在构建的组件(Jar/war文件)，当构建开始时，Gradle会基于build.gradle实例化一个org.gradle.api.Project对象，并通过project变量来隐式调用其成员。

Project属性：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/2d629a2a31ae4f0db073dc999bde0aeb.png)

将build.gradle配置封装为一个Project对象，对象名字为project，通过project可以隐式调用：使用groovy语法

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/bc4d9fea214e430c8b5e86e765db50c3.png)

```
指定仓库位置：默认情况下使用的是中央仓库，此项目如果需要下载jar包从中央仓库中下载到本地目录（C:/Users/zss/.gradle）
mavenCentral()
下载后的内容可以去：C:\Users\zss\.gradle\caches\modules-2\files-2.1中找
但是一般我们习惯使用maven本地仓库：
需要设置maven本地仓库：
```

进行环境变量设置：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/120df4dca5ae4b23804838f46d45e92b.png)

重启IDEA打开，如果需要重新设置maven本地库位置：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/73c8fd0a7a7444d983d43fcacfe380ee.png)

PS：本地仓库的设置对新建项目是生效的

如果需要添加依赖，可以从中央仓库中查找坐标：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/666b8a4bbd3e47c78bb3d3e7ae999824.png)

粘贴过来以后，点击刷新：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/68278e91a5634a3ebb23626035a8223f.png)

build.gradle中内容：

```
plugins {
    id 'java'
}

project.group = 'com.msb'
version '1.0-SNAPSHOT'
/*
指定仓库位置：默认情况下使用的是中央仓库，此项目如果需要下载jar包从中央仓库中下载到本地目录（C:/Users/zss/.gradle）
mavenCentral()
下载后的内容可以去：C:\Users\zss\.gradle\caches\modules-2\files-2.1中找
但是一般我们习惯使用maven本地仓库：
需要设置maven本地仓库：
*/
repositories {
    mavenLocal()
    mavenCentral()
}

dependencies {
    testImplementation 'org.junit.jupiter:junit-jupiter-api:5.6.0'
    testRuntimeOnly 'org.junit.jupiter:junit-jupiter-engine'
    // https://mvnrepository.com/artifact/org.mybatis/mybatis
    implementation group: 'org.mybatis', name: 'mybatis', version: '3.5.9'

}

test {
    useJUnitPlatform()
}

tasks.withType(JavaCompile) {
    options.encoding = "UTF-8"
}
```

PS:Gradle没有自己的中央仓库，用的就是maven的中央仓库

### 4.5.2 Task

每个任务在构建执行过程中会被封装成org.gradle.api.Task对象，主要包括任务的动作和任务依赖，任务动作定义了一个原子操作，可以定义依赖其他任务、动作的顺序、执行的条件。

任务主要操作**动作**：
dependsOn：依赖相关操作
doFirst ：任务执行之前执行的方法
doLast、<<（老版本用，现在废弃了）：任务执行之后执行的方法

**定义好任务后，默认分配在other分组下：**

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/41d4990e62244c84a7fbe85902f26cab.png)

**也可以放在自定义的分组下：**

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/911b96a383e84280b8de386b85487e47.png)

**任务的定义的方式：（6种定义方式）**

```
plugins {
    id 'java'
}

project.group = 'com.msb'
version '1.0-SNAPSHOT'
/*
指定仓库位置：默认情况下使用的是中央仓库，此项目如果需要下载jar包从中央仓库中下载到本地目录（C:/Users/zss/.gradle）
mavenCentral()
下载后的内容可以去：C:\Users\zss\.gradle\caches\modules-2\files-2.1中找
但是一般我们习惯使用maven本地仓库：
需要设置maven本地仓库：
*/
repositories {
    mavenLocal()
    mavenCentral()
}

dependencies {
    testImplementation 'org.junit.jupiter:junit-jupiter-api:5.6.0'
    testRuntimeOnly 'org.junit.jupiter:junit-jupiter-engine'
    // https://mvnrepository.com/artifact/org.mybatis/mybatis
    implementation group: 'org.mybatis', name: 'mybatis', version: '3.5.9'

}

test {
    useJUnitPlatform()
}

tasks.withType(JavaCompile) {
    options.encoding = "UTF-8"
}

//自定义任务：
//定义方式1：
task(t1,{
    group("mytask")
    //配置代码
    println '我是任务1'
    //动作代码
    doFirst {
        println '在任务t1执行前操作的动作代码'
    }
    //动作代码
    doLast {
        println '在任务t1执行后操作的动作代码'
    }
})
//定义方式2：
task t2 {
    group("mytask")
    //配置代码
    println '我是任务2'
    //动作代码
    doFirst {
        println '在任务t2执行前操作的动作代码'
    }
    //动作代码
    doLast {
        println '在任务t2执行后操作的动作代码'
    }
}

//定义方式3：
tasks.create('t3'){
    group("mytask")
    //配置代码
    println '我是任务3'
}

//定义方式4：
tasks.register('t4'){
    group("mytask")
    //配置代码
    println '我是任务4'
}

//定义方式5：
tasks{
    task t5{
        group("mytask")
        //配置代码
        println '我是任务5'
    }
}

//可以一次性定义多个任务-》动态任务定义：
3.times{index ->
    task("task${index}"){
        group("mytask")
        //配置代码
        println 'task${index}'
    }
}
```

**任务依赖：**

```
//任务依赖：
task a{
    doFirst {
        println '我是任务a'
    }
}

task b(dependsOn:a){//代表b任务依赖a任务--->依赖方式通过参数传递
    doFirst {
        println '我是任务b'
    }
}

task c{
    dependsOn 'b'  //依赖方式通过内部设置方式进行依赖
    doFirst {
        println '我是任务c'
    }
}

task d{
    doFirst {
        println '我是任务d'
    }
}

d.dependsOn c   //依赖方式通过外部设置方式进行依赖
```

**任务的执行时机：**

在构建阶段，配置代码是不执行的，在执行阶段，执行动作代码

```
//通过tasks.register定义的任务，在build阶段的配置过程中不执行
//通过tasks.register定义的任务，在任务的执行阶段的配置过程中是执行的
//通过tasks.register定义的任务，配置代码的执行时机是落后于用task方式配置的
```

**定位任务：对某个已有的任务进行扩展：例如对clean内置任务进行扩展**

```
clean.doLast {
    println '我在clean之后执行这个逻辑'
}

tasks.named('clean').get().doFirst {
    println '我在clean之前执行这个逻辑'
}
```

## 4.6 Gradle项目构建生命周期

Gradle的生命周期分三个阶段：初始化阶段、配置阶段,、执行阶段。
**初始化阶段**
通过settings.gradlle判断有哪些项目需要初始化，加载所有需要初始化的项目的build.gradle文件并为每个项目创建project对象
**配置阶段**
执行各项目下的build.gradle脚本，完成project 的配置，并且构造Task任务依赖关系图以便在执行阶段按照依赖关系执行Task中的配置代码
**执行阶段**
通过配置阶段的Task图，按顺序执行需要执行的任务中的动作代码，就是执行任务中写在doFirst或doLast中的代码。

## 4.7 插件

### 4.7.1 添加插件、发布和使用自定义jar包

案例：将自己的项目打成jar包，供给另外的项目使用

（1）新建一个Gradle项目：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/9d1af9561aa646f0a0046a0a1171193a.png)

（2）配置插件：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/7bae6c32d7454a08ab8d9fbfad193494.png)

（3）然后刷新项目，刷新后任务中多了一个分组：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/949bee13bd4a4b7c9f470a8e6ed09136.png)

（4）配置发布分组：在build.gradle中配置：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/ab13f242885143879f0a18dfa400cdbe.png)

(5)执行任务，发布jar包到本地仓库中：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/1848bd76f023486f93b594440cddb7a8.png)

（6）自行去本地库中查找你jar包和生成的配置文件：

C:\Users\zss\.m2\repository\org\example\TestGradleJar

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/fe987143b46c4a84adae607e2ba68369.png)

（7）在其它项目中使用刚才本地库中的jar包：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/799ab1372aa64d31a7b66ebb2369ef51.png)

（8）验证：是否可以使用jar包中内容：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/3007204d70eb45ea91519cd7e9fdb611.png)

### 4.7.2 自定义插件

（1）在构建脚本中直接编写自定义插件：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/f278ee1481e048188231cc8c9d1d1efd.png)

但是上面的方法只能在当前脚本中使用，不可以在整个项目中使用，如果要想在整个项目中的所有构建脚本中都使用的话，需要将任务单独提取出来放入buildSrc下：

（2）自己创建buildSrc目录：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/3995a733e70047f79083d9ae29e2d896.png)

注意点：groovy目录创建好后一定要是蓝色的文件夹，如果是灰色的文件夹，需要自己构建build.gradle脚本，然后加入插件：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/3a7ccda2e30944d79a04b3d90ccf7770.png)

然后定义插件：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/4af0a01ec6ab483ba73f4478c7d372d8.png)

定义好以后，就可以在项目的所有build.gradle中使用了：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/596fbfd50ee84b5eb41d1aef0a761249.png)

## 4.8 Gradle版本冲突问题

**（1）依赖传递性：**

假设你的项目依赖于一个库，而这个库又依赖于其他库。你不必自己去找出所有这些依赖，你只需要加上你直接依赖的库，Gradle会隐式的把这些库间接依赖的库也加入到你的项目中。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/3983a5c5564b407f8d6dc0da468e567c.png)

**（2）传递性依赖中版本冲突：**

由于传递性依赖的特点，两个不同版本的jar包会被依赖进来，这样就存在版本冲突的问题。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/0f987557c2524d8583438f4c9b4884a0.png)

**（3）maven中解决冲突的办法-自动解决方案：**

【1】第一原则：最短路径优先原则

“最短路径优先”意味着项目依赖关系树中路径最短的版本会被使用。

例如，假设A、B、C之间的依赖关系是A->B->C->D(2.0)  和A->E->(D1.0)，那么D(1.0)会被使用，因为A通过E到D的路径更短。

【2】第二原则：最先声明原则

依赖路径长度是一样的的时候，第一原则不能解决所有问题，比如这样的依赖关系：A–>B–>Y(1.0)，A–>C–>Y(2.0)，Y(1.0)和Y(2.0)的依赖路径长度是一样的，都为2。那么到底谁会被解析使用呢？在maven2.0.8及之前的版本中，这是不确定的，但是maven2.0.9开始，为了尽可能避免构建的不确定性，maven定义了依赖调解的第二原则：第一声明者优先。在依赖路径长度相等的前提下，在POM中依赖声明的顺序决定了谁会被解析使用。顺序最靠前的那个依赖优胜。

**（4）Gradle中解决冲突的办法-自动解决方案：**

Gradle的默认自动解决版本冲突的方案是选用版本最高的。

案例：加入两个依赖：

```
implementation group: 'org.springframework', name: 'spring-jdbc', version: '5.1.3.RELEASE'
implementation group: 'org.springframework', name: 'spring-webmvc', version: '5.1.13.RELEASE'

```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/8db8d9b01cb448c39b3cd2e56d0c2eb2.png)

**（5）Gradle中解决冲突的办法-手动修改依赖：**

**手动排除依赖：**

```
dependencies { 
    implementation(group: 'org.springframework', name: 'spring-jdbc', version: '5.1.3.RELEASE'){
        exclude group:'org.springframework',module:'spring-beans'
    }
}
```

后续可以自己手动配置你想要的版本的依赖。

**修改默认配置策略，对所有jar不做冲突自动解决：**

```
configurations.all{
    resolutionStrategy{
        failOnVersionConflict()
    }
}
```

就会在构建时候抛出异常：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/cbd4d14e77664e5cad988f1d33a9d46d.png)

**手动指定某个jar 的版本：**

force:强制覆盖某个版本：

```
configurations.all{
    resolutionStrategy{
        force 'org.springframework:spring-beans:5.3.12'
    }
}
```

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/9615b12e48514926950b432174c2e746.png)


## 4.9 多项目构建

在企业中，一个复杂的项目往往是分成几个小项目来协同完成的，这就涉及到多项目的构建，而多项目构建则需要把一个大项目进行项目模块化，通过模块的互相协作完成整个功能。在之前使用Maven的多项目构建时，一般需要一个root项目来统一管理所有的模块，Gradle也一样使用一个root项目来统一管理所有的模块。


案例：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/273bfa10efae445cb63e4ff4798a9432.png)



构建：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/ed7cc2f6e36b4cf583b303ba5dcfafc2.png)

配置：

配置1：统一插件配置：在根项目的build.gradle中配置：

```
//统一配置信息，包含root项目：
allprojects{
    //写法1：
//    plugins {
//        id 'java'
//    } 
    //写法2：
    apply plugin : 'java'
}
```

配置2：统一配置公共属性：

```

allprojects{
    project.group = 'com.msb'
    version '1.0-SNAPSHOT'
}

```

配置3：配置项目的依赖关系：在子项目的build.gradle中配置：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/cf4ed1b7a5ef4f72a6d819b96c034866.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/20db737e79714573afc6467296730270.png)

验证：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/728/1641366521000/92e936a923d649919f2d5760aae8b39f.png)



配置4：统一资源库：

```
subprojects{
    repositories {
        mavenLocal()
        mavenCentral()
    }
}
```


配置5：配置公用的依赖：配置在根项目的build.gradle中：

```
subprojects{

    dependencies {
        testImplementation 'org.junit.jupiter:junit-jupiter-api:5.6.0'
        testRuntimeOnly 'org.junit.jupiter:junit-jupiter-engine'
    }

}

```


PS：如果配置在subprojects外面，就只针对根生效，对子项目无效，只有放在subprojects中对所有项目生效
