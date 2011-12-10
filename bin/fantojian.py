#!/usr/bin/env python
from jianfan import ftoj
import sys
for line in sys.stdin.readlines():
    print ftoj(line).encode('utf-8').strip()
