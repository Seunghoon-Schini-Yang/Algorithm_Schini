import sys
from heapq import heappop, heappush


def solution(n, paths, gates, summits):
    ans = list()
    gates_set = set(gates)
    summits_set = set(summits)
    INF = sys.maxsize
    graph = [[] for _ in range(n+1)]
    for v1,v2,w in paths:
        graph[v1].append((w,v2))
        graph[v2].append((w,v1))

    for gate in gates:
        maxy = 0
        dist = [INF] * (n+1)
        dist[gate] = 0
        pq = [(0,gate)]
        while pq:
            p_w,p_n = heappop(pq)
            if p_w > dist[p_n]:
                continue
            if p_w > maxy:
                maxy = p_w
            if p_n in summits_set:
                ans.append((maxy, p_n))
                break
            
            for c_w,c_n in graph[p_n]:
                if c_w < dist[c_n] and c_n not in gates_set:
                    heappush(pq, (c_w, c_n))
                    dist[c_n] = c_w

    return list(sorted(ans)[0][::-1])
