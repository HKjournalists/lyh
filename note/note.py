#!/usr/bin/env python
#coding=utf-8
import sys, os
path = os.path.split(os.path.realpath(sys.argv[0]))[0]
if len(sys.argv) == 1:
    print 'error!'
else:
    filename = path+'/'+sys.argv[1]
    if len(sys.argv) == 2:
        print ''
        print open(filename,'r').read()
    else:
        str=''
        for s in sys.argv[2:]:
            str += s+' '
        open(filename,'a').write(str+'\n')
