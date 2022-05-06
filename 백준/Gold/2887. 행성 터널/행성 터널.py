import sys
input = sys.stdin.readline
from heapq import heappush, heappop


def sol(n: int) -> int:
    INF = sys.maxsize
    locs = [0] * n
    edges = [[] for _ in range(n)]
    visited = [0] * n
    dist = [INF] * n
    dist[0] = 0
    pq = [(0,0)]
    w_sum = 0

    for i in range(n):
        locs[i] = (*map(int, input().split()), i)
    
    xyz = zip(sorted(locs), sorted(locs, key=lambda x: x[1]), sorted(locs, key=lambda x: x[2]))
    (pxw,_,_,pxn), (_,pyw,_,pyn), (_,_,pzw,pzn) = next(xyz)
    
    for _ in range(n-1):
        (cxw,_,_,cxn), (_,cyw,_,cyn), (_,_,czw,czn) = next(xyz)
        edges[pxn].append((abs(cxw-pxw), cxn))
        edges[cxn].append((abs(cxw-pxw), pxn))
        edges[pyn].append((abs(cyw-pyw), cyn))
        edges[cyn].append((abs(cyw-pyw), pyn))
        edges[pzn].append((abs(czw-pzw), czn))
        edges[czn].append((abs(czw-pzw), pzn))
        pxw,pxn,pyw,pyn,pzw,pzn = cxw,cxn,cyw,cyn,czw,czn

    while pq:
        p_w,p_n = heappop(pq)
        if p_w > dist[p_n]:
            continue

        visited[p_n] = 1
        w_sum += p_w

        for c_w,c_n in edges[p_n]:
            if visited[c_n] or c_w >= dist[c_n]:
                continue
            heappush(pq, (c_w,c_n))
            dist[c_n] = c_w

    return w_sum


print(sol(int(input())))
