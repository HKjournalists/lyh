#!/usr/bin/env python
#coding=utf-8

'''
从管道读取多行数据,用空格链接为一行输出
'''
import sys
strings = [s.strip() for s in sys.stdin.readlines()]
if len(sys.argv)>1:
    c = sys.argv[1]
else:
    c = ' '
print c.join(strings)
