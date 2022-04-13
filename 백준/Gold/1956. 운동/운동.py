# psj_0708 님 코드 참고
# dynamic programming + priority queue
import sys
input = sys.stdin.readline
import math
from heapq import heappop, heappush

def sol(v: int, e: int) -> int:
    INF = math.inf
    q = list()
    dist_dp = [[INF]*(v+1) for _ in range(v+1)]
    graph = [[] for _ in range(v+1)]

    for _ in range(e):
        a,b,c = map(int, input().split())
        graph[a].append((c,b))
        dist_dp[a][b] = c
        heappush(q, (c,a,b))

    while q:
        c,a,b = heappop(q)
        if a==b:
            return c
        if c > dist_dp[a][b]:
            continue
        for c_c,c_b in graph[b]:
            if c+c_c < dist_dp[a][c_b]:
                dist_dp[a][c_b] = c+c_c
                heappush(q, (c+c_c,a,c_b))

    return -1


print(sol(*map(int, input().split())))
