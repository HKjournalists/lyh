#!/usr/bin/env python
#ecoding=utf-8
import sys

'''
使用提示： 如果没有输入你想要的结果，那么注意以下几个问题
你配置的matchs是否正确？
对于一套matchs匹配的数据他们是否都在一行？
'''
def matchString(content,matchs):
    string = content
    i = 0
    while i < len(matchs):
        start = string.find(matchs[i])
        if start < 0: 
            string = ''
            break
        end = string.find(matchs[i+1],start+len(matchs[i]))
        if end < 0:
            string = ''
            break
        string = string[start+len(matchs[i]):end].strip()
        i = i+2
    return string

def matchAllString(content,matchs):
    results = []
    while len(content) > 0:
        result = matchString(content,matchs)
        if result != '':
            results.append(result)
            content = content.partition(result)[2]
        else:
            content = content.partition(matchs[0])[2]
    return [r.strip() for r in results if r.strip()!='']

if __name__=='__main__':
    matchs = [a for a in sys.argv[1:] if not a.startswith('-')]
    if len(matchs)==0 or len(matchs) % 2==1:
        print 'Usage: lrmatch l1 r1 l2 r2 ...'
    else:
        if '-g' not in sys.argv:
            for line in sys.stdin.readlines():
                print matchString(line,matchs)
        else:
            for line in sys.stdin.readlines():
                print '\n'.join(matchAllString(line,matchs))
