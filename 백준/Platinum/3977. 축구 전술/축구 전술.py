import sys
sys.setrecursionlimit(pow(10, 9))
input = sys.stdin.readline
print = sys.stdout.write
from collections import defaultdict


def dfs(node: int) -> int:
    global odr
    id[node] = rank[node] = odr
    odr += 1
    stack.append(node)

    for cn in graph[node]:
        if finished[cn]:
            g_scc[node].append(cn)
            continue
        if rank[cn] < N:
            if rank[cn] < rank[node]:
                rank[node] = rank[cn]
            continue

        rank_cn = dfs(cn)
        if rank_cn == N:
            g_scc[node].append(cn)
            continue
        if rank_cn < rank[node]:
            rank[node] = rank_cn

    if id[node] == rank[node]:
        finished[node] = True
        while node != (cn := stack.pop()):
            finished[cn] = True
            rank[cn] = rank[node]
        return N

    return rank[node]


if __name__ == '__main__':
    for _ in range(int(input())):
        N,M = map(int, input().split())
        graph = [[] for _ in range(N)]
        for _ in range(M):
            A,B = map(int, input().split())
            graph[A].append(B)

        g_scc = defaultdict(list)
        finished = [False]*N
        rank = [N]*N
        id = [N]*N
        odr = 0

        stack = list()
        for i in range(N):
            if rank[i] < N:
                continue
            dfs(i)

        indgr = {scc:0 for scc in set(rank)}
        for pn in g_scc:
            for cn in g_scc[pn]:
                indgr[rank[cn]] += 1
        
        indgr_zero = [rid for rid,cnt in indgr.items() if not cnt]
        if len(indgr_zero) > 1:
            print('Confused\n')
        else:
            print('\n'.join(map(str, [i for i in range(N) if rank[i]==indgr_zero[0]])))
            print('\n')
        print('\n')
        input()
