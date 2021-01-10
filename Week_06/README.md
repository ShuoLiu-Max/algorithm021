# 学习笔记
##  动态规划：
**本质：记住以往计算过的内容，并再下一次需要的时候直接调用**
如：斐波拉数列
```
fib(n)=fib(n-1)+fib(n-2)
fib(0)=0
fib(1)=1
```
**递归解法**
```
def fib(n):
    if n<=1 :
        return n
    return fib(n-1)+fib(n-2)
print(fib(40))
```

**动态规划(n较大时，动态规划要比递归快得多)**
```
n=81
memo=[]
for i in range(n):
    memo.append(-1)
print(memo)
def fib(n,memo):       # 自顶向下（想要计算fib(n),则需要计算fib(n-1),fib(n-1),计算fib(n-1)需要计算fib(n-2)和fib(n-3)），一般是递归加记忆化搜索
    if n<=1:
        return n
    if memo[n]==-1:
        memo[n]=fib(n-1,memo)+fib(n-2,memo)
    return memo[n]
print(fib(40,memo))
```

**还有一种方法，就是自底向上（计算fib(0）和fib(1)得到fib(2),由fib(1)和fib(2)又得到fib(3),......)
自底向上进行递推，是一种动态规划较为终极的形态。**

### 动态规划的关键点：
#### 1、最优子结构 opt[n] = best_of(opt[n-1],opt[n-2],...)
#### 2、储存中间状态：opt[i]
#### 3、递推公式（状态转移方程或者DP方程）
如：fib：opt[i]=opt[n-1]+opt[n-2]
二维路径：opt[i,j]=opt[i+1][j]+opt[i][j+1] (且判断a[i,j]是否为空地)