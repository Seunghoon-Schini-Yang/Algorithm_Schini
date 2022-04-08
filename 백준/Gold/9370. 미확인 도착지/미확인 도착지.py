import sys
input = sys.stdin.readline
from heapq import heappop, heappush

def sol(nodes: int, edges: int, e_nodes: int) -> str:
    INF = sys.maxsize
    s_node, s_used, e_used = map(int, input().split())
    graph = [{} for _ in range(nodes+1)]
    for _ in range(edges):
        a,b,d = map(int, input().split())
        graph[a][b] = d*2
        graph[b][a] = d*2

    graph[s_used][e_used] -= 1
    graph[e_used][s_used] -= 1

    entire = [INF]*(nodes+1)
    entire[s_node] = 0

    q = list()
    heappush(q, (0,s_node))
    while q:
        p_w,p_n = heappop(q)
        if entire[p_n] < p_w:
            continue
        for c_n,c_w in graph[p_n].items():
            if p_w+c_w < entire[c_n]:
                entire[c_n] = p_w+c_w
                heappush(q, (entire[c_n],c_n))
    
    res = []
    for _ in range(e_nodes):
        k = int(input())
        if entire[k]<INF and entire[k]&1:
            res.append(k)
    res.sort()

    return ' '.join(map(str, res))


print('\n'.join(sol(*map(int, input().split())) for _ in range(int(input()))))
