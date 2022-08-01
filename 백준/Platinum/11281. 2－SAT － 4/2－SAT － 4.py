import sys
sys.setrecursionlimit(pow(10, 9))
input = sys.stdin.readline
from collections import defaultdict


def dfs(node: int) -> int:
    global odr
    id[node] = rank[node] = odr
    odr += 1
    stack.append(node)

    for cn in graph[node]:
        if finished[cn]:
            graph_s[node].append(cn)
            continue
        if rank[cn]:
            if rank[node] > rank[cn]:
                rank[node] = rank[cn]
            continue

        rank_cn = dfs(cn)
        if not rank_cn:
            return False
        if rank_cn == INF:
            graph_s[node].append(cn)
            continue
        if rank[node] > rank_cn:
            rank[node] = rank_cn

    if rank[node] == id[node]:
        chk_set = {node}
        scc[rank[node]].append(node)
        finished[node] = True
        while node != (pn := stack.pop()):
            if -pn in chk_set:
                return False
            chk_set.add(pn)
            scc[rank[node]].append(pn)
            finished[pn] = True
            rank[pn] = rank[node]
        return INF
            
    return rank[node]


def dfs2(node: int) -> None:
    for cn in graph[node]:
        if case[abs(cn)] >= 0:
            continue
        case[abs(cn)] = 0 if cn < 0 else 1
        dfs2(cn)
    return


if __name__ == '__main__':
    N,M = map(int, input().split())
    INF = 2*N + 1
    graph = defaultdict(set)
    for _ in range(M):
        i,j = map(int, input().split())
        if not i+j:
            continue
        graph[-i].add(j)
        graph[-j].add(i)
    
    scc = defaultdict(list)
    graph_s = defaultdict(list)
    finished = [False]*(2*N+1)
    finished[0] = True
    id = [0]*(2*N+1)
    rank = [0]*(2*N+1)
    odr = 1
    stack = list()

    is_poss = True
    for i in range(-N, N+1):
        if finished[i]:
            continue
        if not dfs(i):
            is_poss = False
            break
    print(1 if is_poss else 0)

    if is_poss:
        graph_n = defaultdict(set)
        indgr = defaultdict(int)
        for pn in graph_s:
            for cn in graph_s[pn]:
                if rank[cn] in graph_n[rank[pn]]:
                    continue
                graph_n[rank[pn]].add(rank[cn])
                indgr[rank[cn]] += 1

        q = list()
        for i in graph_n:
            if indgr[i]:
                continue
            q.append(i)

        case = [-1]*(N+1)
        while q:
            pn = q.pop()
            for i in scc[pn]:
                if case[abs(i)] >= 0:
                    continue
                case[abs(i)] = 1 if i < 0 else 0
                dfs2(-i)
            
            for cn in graph_n[pn]:
                indgr[cn] -= 1
                if not indgr[cn]:
                    q.append(cn)

        for i in range(1, N+1):
            if case[i] == -1:
                case[i] = 1
        print(*case[1:])
