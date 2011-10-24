#!/usr/bin/env python

import sys
if len(sys.argv) > 1:
    strings =[]
    for fileName in sys.argv[1:]:
        strings += open(fileName).readlines()
else:
    strings = [s.strip() for s in sys.stdin.readlines()]
print '\r\n'.join(s.strip() for s in strings)
