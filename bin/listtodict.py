#!/usr/bin/env python
import sys
for line in sys.stdin.readlines():
    if line.count('[') == line.count(']') == 1:
        out = ''
        for key in line.partition('[')[2].partition(']')[0].split(','):
            if len(key.strip()) > 0:
                out += key.strip()+":'', "
        print '{%s}' % out
