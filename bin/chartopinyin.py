#!/usr/bin/env python

import sys, os
filePath = os.path.split(os.path.realpath(__file__))[0]
d = dict([l.split('\t') for l in open(filePath + '/pinyin.dat').readlines()])

def charToPinyin(chars):
    result = []
    for char in unicode(chars, 'utf-8', 'ignore'):
        key = "%X" % ord(char)
        try:
            result.append(d[key].split(" ")[0].strip()[:-1].lower())
        except:
            result.append(char)
    return ''.join(result)


if __name__=='__main__':
    for line in sys.stdin.readlines():
        print charToPinyin(line).strip()
