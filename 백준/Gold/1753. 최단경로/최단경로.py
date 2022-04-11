import sys
input = sys.stdin.readline
from heapq import heappop, heappush
import math

def sol(v: int, e: int, s: int) -> str:
    INF = math.inf
    is_inf = math.isinf
    shortest = [INF]*(v+1)
    shortest[s] = 0
    graph = [[] for _ in range(v+1)]
    visited = set()

    for _ in range(e):
        n_1,n_2,w  = map(int, input().split())
        graph[n_1].append((w,n_2))

    heap = [(0,s)]

    while heap:
        w,n = heappop(heap)
        visited.add(n)
        for c_w,c_n in graph[n]:
            if c_n not in visited and w+c_w < shortest[c_n]:
                shortest[c_n] = w+c_w
                heappush(heap, (shortest[c_n],c_n))
                
    return '\n'.join('INF' if is_inf(dist) else str(dist) for dist in shortest[1:])


print(sol(*map(int, input().split()), int(input())))
