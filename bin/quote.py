#!/usr/bin/env python

import sys
from urllib import quote

if __name__=='__main__':
    for line in sys.stdin.readlines():
        sys.stdout.write( quote(line.strip()) )

