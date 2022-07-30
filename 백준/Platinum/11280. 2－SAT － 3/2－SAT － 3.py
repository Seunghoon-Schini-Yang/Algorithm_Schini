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
            continue
        if rank[cn]:
            if rank[node] > rank[cn]:
                rank[node] = rank[cn]
            continue

        rank_cn = dfs(cn)
        if not rank_cn:
            return False
        if rank_cn == INF:
            continue
        if rank[node] > rank_cn:
            rank[node] = rank_cn

    if rank[node] == id[node]:
        chk_set = {node}
        finished[node] = True
        while node != (pn := stack.pop()):
            if -pn in chk_set:
                return False
            chk_set.add(pn)
            finished[pn] = True
            rank[pn] = rank[node]
            
    return rank[node]


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
    
    finished = defaultdict(bool)
    id = defaultdict(int)
    rank = defaultdict(int)
    odr = 1
    stack = list()

    is_poss = True
    for i in range(1, N+1):
        if not graph[i]:
            continue
        if not dfs(i):
            is_poss = False
            break
    print(1 if is_poss else 0 )
