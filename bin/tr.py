#!/usr/bin/env python
#coding=utf-8
# 翻译程序
# Usage: tr word
import sys, httplib2, os
from urllib import urlencode

path = os.path.split(os.path.realpath(sys.argv[0]))[0]

def tran(searchWord):
    searchWord = urlencode({'text':searchWord})
    url = r'http://translate.google.cn/translate_a/t?client=t&'+searchWord+r'&hl=zh-CN&sl=en&tl=zh-CN&otf=1&pc=0'
    h = httplib2.Http(path+'/.translatecache')
    headers = {'User-Agent':'Mozilla/5.0 (X11; U; Linux i686; zh-CN; rv:1.9.0.18) Gecko/2010021720 Iceweasel/3.0.6 (Debian-3.0.6-3)'}
    response, content = h.request(url, headers = headers)
    print ''
    print content[content.find('{"trans":"')+len('{"trans":"'):content.find('","orig":"')]
    if content.find('"dict":[{') != -1:
        others = content[content.find('"dict":[{')+len('"dict":[{'):content.find('}],"src"')]
        print others.replace('},{','\n').replace('"pos":','').replace('"terms":','').replace('"','').replace(',[',':  ').replace(']','')



if len(sys.argv) ==1:
    searchWord = sys.stdin.readline()
    while searchWord != '\n':
        tran(searchWord.strip())
        searchWord = sys.stdin.readline()
else:
    searchWord = ''
    for s in sys.argv[1:]:
        searchWord += s+' '
    tran(searchWord[:-1])
