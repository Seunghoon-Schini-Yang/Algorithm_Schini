import sys
input = sys.stdin.readline
from heapq import heappop, heappush

def sol(n: int, m: int) -> str:
    INF = sys.maxsize
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int, input().split())
        graph[a].append((c,b))
    start,end = map(int, input().split())
    dist = [INF] * (n+1)
    dist[start] = 0
    path = [0] * (n+1)
    q = [(0,start)]

    while q:
        p_c,p_n = heappop(q)
        if p_c > dist[p_n]:
            continue
        
        for c_c,c_n in graph[p_n]:
            n_c = p_c+c_c
            if n_c < dist[c_n]:
                dist[c_n] = n_c
                path[c_n] = p_n
                heappush(q, (n_c,c_n))

    temp = str(dist[end])
    ans = [str(end)]
    while path[end]:
        end = path[end]
        ans.append(str(end))

    return '\n'.join((temp, str(len(ans)), ' '.join(reversed(ans))))


print(sol(int(input()), int(input())))
