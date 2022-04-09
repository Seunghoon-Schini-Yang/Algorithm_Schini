# https://velog.io/@jajubal/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EB%B0%B1%EC%A4%80-1540-%ED%8A%B9%EC%A0%95%ED%95%9C%EC%B5%9C%EB%8B%A8%EA%B2%BD%EB%A1%9C
# 블로그에서 정답이라고 하는 코드
# 내 생각엔 틀렸습니다 나올 것 같은데, 정답이라고 해서 확인해보려고 복붙함
import sys; input = sys.stdin.readline
from heapq import heappush, heappop

def dijkstra(start, end):
    dis = [0xffffff] * (N + 1)
    dis[start] = 0
    q = [[0, start]]
    while q:
        k, u = heappop(q)
        if k > dis[u]: continue
        for w, v in G[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                heappush(q, [dis[v], v])

    return dis[end]

N, E = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append([w, v])
    G[v].append([w, u])

stop1, stop2 = map(int, input().split())

# 1 -> stop1 -> stop2 -> N
path1 = dijkstra(1, stop1) + dijkstra(stop1, stop2) + dijkstra(stop2, N)
# 1 -> stop2 -> stop1 -> N
path2 = dijkstra(1, stop2) + dijkstra(stop2, stop1) + dijkstra(stop1, N)

if path1 >= 0xffffff and path2 >= 0xffffff:
    print(-1)
else:
    print(min(path1, path2))