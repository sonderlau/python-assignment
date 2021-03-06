# 11-03 第二次作业

## 7-1 杭州阶梯电价

杭州实行一户一表并阶梯电价制：月用量超过 230kw 以内的，电价为 0.538 元；超过 230kw 并在 400kw 以内的，超出部分电价上涨 0.05 元；超过 400kw 的超出部分再上涨 0.3 元。编写程序，当输入某用户使用月电量，输出该用户月电费总价(输入为整数，输出保留两位小数）

### 输入格式:

在提示信息同一行输入大于零的月电量。

### 输出格式:

输出月电费。

### 输入样例:

```
300
```

### 输出样例:

```
164.90
```

参考 [7-1](./7-1.py)



## 7-2 平均值

在一行上输入若干整数，每个整数以一个空格分开，求这些整数的平均值。

### 输入格式:

首先输入一个正整数 T，表示测试数据的组数，然后是 T 组测试数据。每组测试输入一个字符串（仅包含数字字符和空格）。

### 输出格式:

对于每组测试，输出以空格分隔的所有整数的平均值，结果保留一位小数。

### 输入样例:
```
1
1 2 3 4 5 6 7 8 9 10
```

### 输出样例:
```
5.5
```

参考 [7-2](./7-2.py)



## 7-3 五位以内的对称素数

判断一个数是否为对称且不大于五位数的素数。要求判断对称和判断素数各写一个函数。

### 输入格式:
测试数据有多组，处理到文件尾。每组测试输入一个正整数 n（$0 < n < 2^{32}$）。



### 输出格式:

对于每组测试，若 n 是不大于五位数的对称素数，则输出“Yes”，否则输出“No”。

每个判断结果单独占一行。

注意：引号不必输出。



### 输入样例:
```
11
101
272
33533
2147483647
```

### 输出样例:
```
Yes
Yes
No
Yes
No
```

参考 [7-3](./7-3.py)



## 7-4 分支结构——大小写字母判断

键盘输入一个英文字母，如果是大写字母，输出 ASCII 码，如果是小写字母输出对应的大写字母。（其它情况没有输出）



### 输入格式:

输入一个英文字母。



### 输出格式:
根据输入的字母，输出 ASCII 码或者大写字母



### 输入样例 1:
```
A
```
### 输出样例 1:

```
65
```



### 输入样例 2:

```
a
```

### 输出样例 2:

```
A
```



参考 [7-4](./7-4.py)



## 7-5 求 n 个数中的最大值

用户先输入一个正整数 N（N 不超过 10），表示将下来将输入 N 个整数（均为 int 型），请在这 N 个整数中找出最大值。



### 输入格式:
输入为一行，第一个是正整数 N，然后是 N 个整数。



### 输出格式:
输出为一个整数，表示 N 个整数中的最大值。



### 输入样例 1:
```
4 2 123 -100 0
```

### 输出样例 1:
```
123
```



### 输入样例 2:

```
3 -9 -18 -28
```

### 输出样例 2:
```
-9
```



参考 [7-5](./7-5.py)



## 7-6 计算平方和

编写一个程序，要求用户输入一个下限整数和一个上限整数，然后，依次计算从下限到上限的每一个数的平方的和，最后显示结果。程序将不断要求用户输入下限整数和上限整数并显示出答案，直到用户输入的上限整数等于或小于下限整数为止。



### 输入格式:

程序将不断要求用户输入下限整数和上限整数并显示出答案，直到用户输入的上限整数等于或小于下限整数为止。

每次输入一对整数，分别是下限和上限。当输入的上限等于或小于下限时结束。



### 输出格式:
从下限到上限的每个整数的平方和。



### 输入样例 1:
```
5 9
3 25
5 3
```

### 输出样例 1:
```
The sum of the squares from 25 to 81 is 255
The sum of the squares from 9 to 625 is 5520
Done
```



### 输入样例 2:

```
9 7
```

### 输出样例 2:
```
Done
```



参考 [7-6](./7-6.py)



## 7-7 计算 m 到 n 之间自然数数列的和

计算 m~n(m<=n)之间自然数数列的和。如 m 和 n 如果是 3 和 10，则是求数列 3+4+5+......+9+10 的和。



### 输入格式:

在一行中输入 2 个正整数 m 和 n，0<=m<=n。



### 输出格式:
输出数列和。



### 输入样例:

```
3 10
```



### 输出样例:

在这里给出相应的输出。例如：

```
sum = 52
```



参考 [7-7](./7-7.py)
