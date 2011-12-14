#!/usr/bin/env python
import sys

queue = []

for l in sys.stdin.readlines():
    l = l.replace('\t',' ')
    assert(';' not in l)
    space_len = len(l)-len(l.lstrip())
    l = l.strip()
    if len(queue) == 0:
        queue.append((space_len, l))
    else:
        if space_len > queue[-1][0]:
            queue.append((space_len, l))
        elif space_len == queue[-1][0]:
            queue[-1] = (space_len, l)
        else:
            while len(queue)>0 and space_len <= queue[-1][0]:
                queue.pop()
            queue.append((space_len, l))

    print ';'.join([q[1] for q in queue])
