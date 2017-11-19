# Fibonacci
##  函数 **Fibonacci**
使用递归进行计算。T<sub>n</sub> = O(2<sup>n</sup>)，S<sub>n</sub> = O(n)。

## 函数 **Fibonacci_1**
由于 F(n) = F(n-1) + F(n-2)，
于是，Fibonacci_1(n) 返回 一个 F(n) 和 F(n-1) 的 list，
于是，就不需要重复计算树的右侧叶子。T<sub>n</sub> = O(n)，S<sub>n</sub>。


## 函数 **Fibonacci_2**
对于每个n，F(n)只计算一次。T<sub>n</sub> = O(n)，S<sub>n</sub> = O(n)。

## 函数 **Fibonacci_3**
T<sub>n</sub> = O(n)，S<sub>n<sub> = O(1)。

## 函数 **matrix4And4Multiplication**
函数用来计算2*2矩阵乘以2*2矩阵。

## 函数 **matrix4And2Multiplication**
函数用来计算2*2矩阵乘以1*2矩阵。

## 函数 **matrixPower**
函数用来计算矩阵的n次方。

## 函数 **Fibonacci_4**
函数通过矩阵计算Fibonacci序列。

```
[Fn]   = [1 1] ^n      [1]
                    *
[Fn-1]   [1 0]         [0]
```
T<sub>n</sub> = O(n)，S<sub>n</sub> = O(n-1)。

## 函数 **Fibonacci_5**
A<sup>n</sup>，如果n为奇数，则 A<sup>n</sup> = A<sup>n/2</sup> * A<sup>n/2</sup> * A，如果n为偶数，
A<sup>n</sup> = A<sup>n/2</sup> * A<sup>n/2</sup>。
T<sub>n</sub> = O(log<sup>n</sup>，S<sub>n</sub> = O(log<sup>n</sup>)。

## 函数 **Fibonacci_5**
T<sub>n</sub> = O(log<sup>n</sup>，S<sub>n</sub> = O(log<sup>n</sup>)。
