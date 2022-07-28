import sys
sys.setrecursionlimit(pow(10, 9))
input = sys.stdin.readline
from collections import defaultdict, deque


def dfs(node: int) -> int:
    global odr
    id[node] = rank[node] = odr
    odr += 1
    stack.append(node)

    for cn in graph[node]:
        if finished[cn]:
            scc_edge[node].append(cn)
            continue
        if rank[cn] < N:
            if rank[cn] < rank[node]:
                rank[node] = rank[cn]
            continue

        rank_cn = dfs(cn)
        if rank_cn == N:
            scc_edge[node].append(cn)
            continue
        if rank_cn < rank[node]:
            rank[node] = rank_cn

    if id[node] == rank[node]:
        finished[node] = True
        scc_cash[rank[node]] += cash[node]
        while node != (cn := stack.pop()):
            finished[cn] = True
            scc_cash[rank[node]] += cash[cn]
            rank[cn] = rank[node]
        return N

    return rank[node]


if __name__ == '__main__':
    N,M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        S,P = map(int, input().split())
        graph[S].append(P)
    cash = [0] + [int(input()) for _ in range(1, N+1)]
    S,P = map(int, input().split())
    restr = list(map(int, input().split()))

    scc_edge = defaultdict(list)
    scc_cash = defaultdict(int)
    finished = [False]*(N+1)
    id = [N]*(N+1)
    rank = [N]*(N+1)
    odr = 0
    stack = list()
    dfs(S)

    indgr = {i:0 for i in set(rank[1:]) if i != N}
    graph = defaultdict(set)
    for pn in scc_edge:
        for cn in scc_edge[pn]:
            if rank[cn] in graph[rank[pn]]:
                continue
            graph[rank[pn]].add(rank[cn])
            indgr[rank[cn]] += 1
    
    is_restr = defaultdict(bool)
    for i in restr:
        is_restr[rank[i]] = True

    memo = defaultdict(int)
    memo[rank[S]] += scc_cash[rank[S]]
    q = deque([rank[S]])
    while q:
        pn = q.popleft()
        for cn in graph[pn]:
            indgr[cn] -= 1
            if memo[cn] < memo[pn] + scc_cash[cn]:
                memo[cn] = memo[pn] + scc_cash[cn]
            if indgr[cn]:
                continue
            q.append(cn)

    print(max(cash for pn, cash in memo.items() if is_restr[pn]))
