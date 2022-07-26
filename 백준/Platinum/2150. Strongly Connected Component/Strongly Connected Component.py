import sys
sys.setrecursionlimit(pow(10, 9))
input = sys.stdin.readline


def dfs(node: int) -> int:
    global rank
    stack.append(node)
    node_id[node] = node_rank[node] = rank
    rank += 1

    for c_n in graph[node]:
        if node_rank[c_n] == -1:
            continue
        if node_rank[c_n] < INF:
            if node_rank[c_n] < node_rank[node]:
                node_rank[node] = node_rank[c_n]
            continue
        node_rank[node] = min(dfs(c_n), node_rank[node])

    if node_rank[node] == node_id[node]:
        node_rank[node] = -1
        c_scc = [node]
        while node != (p_n := stack.pop()):
            node_rank[p_n] = -1
            c_scc.append(p_n)
        
        c_scc.sort()
        c_scc.append(-1)
        scc.append(c_scc)
        return INF
    
    return node_rank[node]


if __name__ == '__main__':
    INF = sys.maxsize
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        A,B = map(int, input().split())
        graph[A].append(B)

    scc = list()
    node_rank = [INF]*(V+1)
    node_id = [INF]*(V+1)
    rank = 0
    for i in range(1, V+1):
        if node_rank[i] < INF:
            continue
        stack = list()
        dfs(i)

    scc.sort()
    print(len(scc))
    print('\n'.join(' '.join(map(str, c_scc)) for c_scc in scc))
