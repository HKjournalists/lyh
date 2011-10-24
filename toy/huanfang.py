#coding=utf-8
'''
输出一个n*n的矩阵，要求每一行每一列加起来的和都一样
方法: 移动法
方法发现者: 刘永辉  sdjllyh@gmail.com
方法步骤：
1 用1到n顺序构建矩阵
如:
[1,2,3]
[4,5,6]
[7,8,9]
2 行移动
3 行列转换
4 行移动

行移动步骤为:
移动第一行的右边一个到左边
移动第二行的右边两个到左边
...
移动第n行的右边n个(或n-1个，如果n是奇数，跳过中间行)到左边.

python代码如下!
'''
print '输入n?'
import sys
n = sys.stdin.readline()
n = int(n)
l=[]

#得到:
#[1,2,3]
#[4,5,6]
#[7,8,9]
for i in range(n):
    l.append([])
    for j in range(n):
        l[i].append(n*i+j+1)

#行移动为:
#[3,1,2]
#[4,5,6]
#[8,9,7]
if n%2 == 1:
    for i in range(n):
        if i < n/2: l[i] = l[i][n-i-1:]+l[i][:n-i-1]
        elif i > n/2:  l[i] = l[i][n-i:]+l[i][:n-i]
else:
    for i in range(n):
        l[i] = l[i][n-i-1:]+l[i][:n-i-1]
    

#行列转换:
#[3,4,8]
#[1,5,9]
#[2,6,7]
tmpL = []
for i in range(n): tmpL.append([])
for i in range(n):
    for j in range(n):
        tmpL[i].append(l[j][i])
l = tmpL

#行移动:
#[8,3,4]
#[1,5,9]
#[6,7,2]
if n%2 == 1:
    for i in range(n):
        if i < n/2: l[i] = l[i][n-i-1:]+l[i][:n-i-1]
        elif i > n/2:  l[i] = l[i][n-i:]+l[i][:n-i]
else:
    for i in range(n):
        l[i] = l[i][n-i-1:]+l[i][:n-i-1]

#打印结果
print '每行每列加起来都是'+str(sum(l[0]))
for i in range(n): print l[i]
