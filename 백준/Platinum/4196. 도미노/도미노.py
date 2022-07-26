import sys
sys.setrecursionlimit(pow(10, 9))
input = sys.stdin.readline
from collections import defaultdict


def dfs(node: int) -> int:
    global odr
    stack.append(node)
    rank[node] = id[node] = odr
    odr += 1

    for c_n in graph[node]:
        if finished[c_n]:
            dd_scc[node].append(c_n)
            continue
            
        if rank[c_n] < INF:
            if rank[c_n] < rank[node]:
                rank[node] = rank[c_n]
            continue

        rank_cn = dfs(c_n)
        if rank_cn == INF:
            dd_scc[node].append(c_n)
            continue
        rank[node] = min(rank_cn, rank[node])

    if rank[node] == id[node]:
        finished[node] = True
        while node != (c_n := stack.pop()):
            rank[c_n] = rank[node]
            finished[c_n] = True
        return INF

    return rank[node]


def dfs_scc(node: int) -> None:
    for c_n in graph_scc[node]:
        if id[c_n] == 2:
            continue
        id[c_n] = 2
        if id[c_n] == 1:
            continue
        dfs_scc(c_n)
    return


if __name__ == '__main__':
    INF = sys.maxsize

    for _ in range(int(input())):
        n,m = map(int, input().split())
        graph = [[] for _ in range(n+1)]
        for _ in range(m):
            x,y = map(int, input().split())
            graph[x].append(y)
        
        finished = [False]*(n+1)
        stack = list()
        id = [0]*(n+1)
        rank = [INF]*(n+1)
        odr = 0
        dd_scc = defaultdict(list)

        for i in range(1, n+1):
            if rank[i] < INF:
                continue
            dfs(i)

        graph_scc = defaultdict(list)
        for key, val in dd_scc.items():
            for vtx in val:
                graph_scc[rank[key]].append(rank[vtx])

        ans = 0
        id = [0]*(n+1)
        for scc_i in set(rank[1:]):
            if id[scc_i]:
                continue
            id[scc_i] = 1
            dfs_scc(scc_i)
        print(sum(i for i in id if i==1))
        