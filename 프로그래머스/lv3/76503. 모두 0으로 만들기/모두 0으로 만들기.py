import sys
sys.setrecursionlimit(pow(10, 9))


def solution(a, edges):
    def dfs(pn, n):
        for cn in graph[n]:
            if cn == pn:
                continue
            dfs(n, cn)
            a[n] += a[cn]
            answer[0] += abs(a[cn])
    

    answer = [0]
    graph = [[] for _ in range(len(a))]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    dfs(-1, 0)
    return -1 if a[0] else answer[0]
