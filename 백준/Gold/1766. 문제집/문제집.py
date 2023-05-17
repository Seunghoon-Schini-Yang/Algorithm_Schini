# topological sort + bfs + heap
import sys
input = sys.stdin.readline
print = sys.stdout.write
from heapq import heappop, heappush


def sol(n: int, m: int) -> str:
    graph = [[] for _ in range(n+1)]
    indgr = [0]*(n+1)

    for _ in range(m):
        f,b = map(int, input().split())
        graph[f].append(b)
        indgr[b] += 1

    hq = list()
    for i in range(1, n+1):
        if not indgr[i]:
            heappush(hq, i)

    while hq:
        v = heappop(hq)
        print(f'{v} ')
        for node in graph[v]:
            indgr[node] -= 1
            if not indgr[node]:
                heappush(hq, node)
    return


sol(*map(int, input().split()))
