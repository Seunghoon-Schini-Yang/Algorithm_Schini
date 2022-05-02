# bfs
import sys
from collections import deque

def sol(n: int, k: int) -> int:
    if n >= k:
        return n-k
    
    miny = sys.maxsize
    dist = dict()
    d = dist[n] = 1
    q = deque([n])

    while q:
        p = q.pop()
        d = dist[p]

        if miny <= d:
            return miny-1
        if p == k:
            return dist[p] - 1

        if not dist.get(p*2, False):
            dist[p*2] = d
            if p*2 < k:
                q.append(p*2)
            elif d + p*2 - k < miny:
                miny = d + p*2 - k
        
        if 0 <= p-1 and not dist.get(p-1, False):
            dist[p-1] = d+1
            q.appendleft(p-1)

        if not dist.get(p+1, False):
            dist[p+1] = d+1
            q.appendleft(p+1)


print(sol(*map(int, input().split())))
