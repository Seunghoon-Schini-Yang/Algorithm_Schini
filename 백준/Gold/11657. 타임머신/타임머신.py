# my, bellman ford
import sys
input = sys.stdin.readline
import math

def sol(n: int, m: int) -> str:
    INF = math.inf
    isinf = math.isinf

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int, input().split())
        graph[a].append((c,b))
    
    dijkstra_one = [INF]*(n+1)
    dijkstra_one[1] = 0

    is_update = 0
    for k in range(n):
        for p_n in range(1,n+1):
            for c_w,c_n in graph[p_n]:
                if dijkstra_one[p_n]+c_w < dijkstra_one[c_n]:
                    if k==n-1:
                        return -1
                    dijkstra_one[c_n] = dijkstra_one[p_n]+c_w
                    is_update = 1
        if not is_update:
            break

    
    return '\n'.join(map(lambda x: '-1' if isinf(x) else str(x), dijkstra_one[2:]))


print(sol(*map(int, input().split())))
