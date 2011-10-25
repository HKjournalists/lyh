#!/usr/bin/env python
#coding=utf-8
import sys

strings = [s.strip() for s in sys.stdin.readlines()]
if len(sys.argv)>1:
    c = sys.argv[1]
else:
    c = ' '
for s in strings:
    print '\n'.join(s.split(c))
