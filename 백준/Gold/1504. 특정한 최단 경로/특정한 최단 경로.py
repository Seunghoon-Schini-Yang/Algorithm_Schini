# 1 - n - via1 - via2 - n 의 경우처럼
# 중간 경유 노드를 모두 지나기 전에 n 을 지나가면 안 되는줄 알음
# 그래서 삽질.... 후....
import sys
input = sys.stdin.readline
from heapq import heappop, heappush
import math

def sol(n: int, e: int) -> int:
    INF = math.inf

    graph = [[] for _ in range(n+1)]
    for _ in range(e):
        v1,v2,w = map(int, input().split())
        graph[v1].append((w,v2))
        graph[v2].append((w,v1))
    
    via1, via2 = map(int, input().split())
    if via1>via2:
        via1,via2 = via2,via1

    via1_dist, via2_dist = [INF]*(n+1), [INF]*(n+1)
    via1_dist[via1] = via2_dist[via2] = 0

    pq = list()
    
    heappush(pq, (0,via1))
    while pq:
        p_w,p_n = heappop(pq)
        if via1_dist[p_n] < p_w:
            continue
        for c_w,c_n in graph[p_n]:
            if p_w+c_w < via1_dist[c_n]:
                via1_dist[c_n] = p_w+c_w
                heappush(pq, (via1_dist[c_n], c_n))

    heappush(pq, (0,via2))
    while pq:
        p_w,p_n = heappop(pq)
        if via2_dist[p_n] < p_w:
            continue
        for c_w,c_n in graph[p_n]:
            if c_n==via1:
                continue
            if p_w+c_w < via2_dist[c_n]:
                via2_dist[c_n] = p_w+c_w
                heappush(pq, (via2_dist[c_n], c_n))
    if via1_dist[1]+via1_dist[via2] < via2_dist[1]: 
        via2_dist[1] = via1_dist[1]+via1_dist[via2]
    if via2!=n and via1_dist[n]+via1_dist[via2] < via2_dist[n]:
        via2_dist[n] = via1_dist[n]+via1_dist[via2]
        
    
    ans = min(via1_dist[1]+via1_dist[via2]+via2_dist[n], via2_dist[1]+via1_dist[via2]+via1_dist[n])
    return -1 if math.isinf(ans) else ans


print(sol(*map(int, input().split())))
