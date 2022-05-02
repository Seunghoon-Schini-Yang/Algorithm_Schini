# bfs
import sys
from collections import deque

def sol(n: int, k: int) -> int:
    if n >= k:
        return n-k
    
    miny = sys.maxsize
    visited = dict()
    visited[n] = False
    q = deque([(0,n)])

    while q:
        d,p = q.pop()
        if miny <= d:
            return miny
        if p == k:
            return d

        if visited.get(p*2, True):
            visited[p*2] = False
            if p*2 < k:
                q.append((d,p*2))
            elif d + p*2 - k < miny:
                miny = d + p*2 - k
        
        if 0 <= p-1 and visited.get(p-1, True):
            visited[p-1] = False
            q.appendleft((d+1,p-1))

        if visited.get(p+1, True):
            visited[p+1] = False
            q.appendleft((d+1,p+1))


print(sol(*map(int, input().split())))
