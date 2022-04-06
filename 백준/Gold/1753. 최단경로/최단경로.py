import sys
input = sys.stdin.readline
from heapq import heappop, heappush, heapify

def sol(v: int, e: int, s: int) -> str:
    INF = sys.maxsize
    shortest = [INF]*(v+1)
    graph = [[] for _ in range(v+1)]

    for _ in range(e):
        n_1, n_2, w  = map(int, input().split())
        graph[n_1].append((w,n_2))

    heap = [(0,s)]
    heapify(heap)

    while heap:
        w, n = heappop(heap)
        if w < shortest[n]:
            shortest[n] = w
            for c_w, c_n in graph[n]:
                heappush(heap, (w+c_w,c_n))

    return '\n'.join(str(dist) if dist<INF else 'INF' for dist in shortest[1:])


print(sol(*map(int, input().split()), int(input())))
