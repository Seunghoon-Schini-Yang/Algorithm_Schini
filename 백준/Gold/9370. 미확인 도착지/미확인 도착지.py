import sys
input = sys.stdin.readline
from heapq import heappop, heappush

def sol(nodes: int, edges: int, e_nodes: int) -> str:
    INF = sys.maxsize
    s_node, s_used, e_used = map(int, input().split())
    graph = [[] for _ in range(nodes+1)]
    for _ in range(edges):
        a,b,d = map(int, input().split())
        graph[a].append((d,b))
        graph[b].append((d,a))

    for c_w,c_n in graph[s_used]:
        if c_n==e_used:
            used_w = c_w
            break

    entire, from_s, from_e = [INF]*(nodes+1), [INF]*(nodes+1), [INF]*(nodes+1)
    entire[s_node] = from_s[s_used] = from_e[e_used] = 0

    q = list()
    heappush(q,(0,s_node))
    while q:
        p_w,p_n = heappop(q)
        if entire[p_n] < p_w:
            continue
        for c_w,c_n in graph[p_n]:
            if entire[p_n]+c_w < entire[c_n]:
                entire[c_n] = entire[p_n]+c_w
                heappush(q, (entire[c_n],c_n))

    heappush(q,(0,s_used))
    while q:
        p_w,p_n = heappop(q)
        if from_s[p_n] < p_w:
            continue
        for c_w,c_n in graph[p_n]:
            if c_n==s_node or c_n==e_used:
                continue
            if from_s[p_n]+c_w < from_s[c_n]:
                from_s[c_n] = from_s[p_n]+c_w
                heappush(q, (from_s[c_n],c_n))

    heappush(q,(0,e_used))
    while q:
        p_w,p_n = heappop(q)
        if from_e[p_n] < p_w:
            continue
        for c_w,c_n in graph[p_n]:
            if c_n==s_node or c_n==s_used:
                continue
            if from_e[p_n]+c_w < from_e[c_n]:
                from_e[c_n] = from_e[p_n]+c_w
                heappush(q, (from_e[c_n],c_n))
    
    res = []
    for _ in range(e_nodes):
        k = int(input())
        if used_w + min(entire[s_used]+from_e[k], entire[e_used]+from_s[k]) <= entire[k]:
            res.append(k)
    res.sort()

    return ' '.join(map(str, res))


print('\n'.join(sol(*map(int, input().split())) for _ in range(int(input()))))
