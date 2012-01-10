#!/usr/bin/env python
#coding=utf-8
import sys

strings = ["'" + s.strip().partition(' ')[0] + "'," for s in sys.stdin.readlines()]
print ''.join(strings)

