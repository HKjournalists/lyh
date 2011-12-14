#!/usr/bin/env python

import sys

d = dict([l.split('\t') for l in open('Mandarin.dat').readlines()])

def _chartopinyin(chars):
    result = []
    for char in unicode(chars, 'utf-8', 'ignore'):
        key = "%X" % ord(char)
        try:
            result.append(d[key].split(" ")[0].strip()[:-1].lower())
        except:
            result.append(char)
    return ''.join(result)


if __name__=='__name__':
    for line in sys.stdin.readlines():
        print _chartopinyin(line).strip()
