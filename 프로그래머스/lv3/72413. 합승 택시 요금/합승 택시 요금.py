import sys
from heapq import heappop, heappush


def solution(n, s, a, b, fares):
    def dijkstra(x, d):
        pq = [(0, x)]
        while pq:
            nd, nn = heappop(pq)
            if d[nn] < nd:
                continue
            d[nn] = nd
            for cd, cn in graph[nn]:
                if d[cn] <= nd+cd:
                    continue
                heappush(pq, (nd+cd, cn))
        return d
    
    
    INF = sys.maxsize
    graph = [[] for _ in range(n+1)]
    for x, y, d in fares:
        graph[x].append((d, y))
        graph[y].append((d, x))
    aa = [INF] * (n+1)
    bb = [INF] * (n+1)
    ss = [INF] * (n+1)
    aa[a] = bb[b] = ss[s] = 0
    
    aa = dijkstra(a, aa)
    bb = dijkstra(b, bb)
    ss = dijkstra(s, ss)
    return min(ss[i] + aa[i] + bb[i] for i in range(1, n+1))
