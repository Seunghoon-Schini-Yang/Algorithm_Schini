import sys
sys.setrecursionlimit(pow(10, 9))
input = sys.stdin.readline


def dfs(node: int) -> None:
    is_visited[node] = True
    for c_n in graph[node]:
        if is_visited[c_n]:
            continue
        dfs(c_n)
    stack.append(node)
    return


def dfs_rev(node: int) -> None:
    is_visited[node] = True
    for c_n in graph_rev[node]:
        if is_visited[c_n]:
            continue
        scc[-1].append(c_n)
        dfs_rev(c_n)
    return


if __name__ == '__main__':
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    graph_rev = [[] for _ in range(V+1)]
    for _ in range(E):
        A,B = map(int, input().split())
        graph[A].append(B)
        graph_rev[B].append(A)
    
    is_visited = [False]*(V+1)
    stack = list()
    for i in range(1, V+1):
        if is_visited[i]:
            continue
        dfs(i)

    scc = list()
    is_visited = [False]*(V+1)
    for i in range(len(stack)-1, -1, -1):
        if is_visited[stack[i]]:
            continue
        scc.append([stack[i]])
        dfs_rev(stack[i])
        scc[-1].sort()
        scc[-1].append(-1)
    scc.sort()
    print(len(scc))
    print('\n'.join(' '.join(map(str, scc_elem)) for scc_elem in scc))
