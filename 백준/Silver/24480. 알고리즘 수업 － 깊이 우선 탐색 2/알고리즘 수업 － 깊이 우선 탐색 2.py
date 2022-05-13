import sys
input = sys.stdin.readline


def sol(n: int, m: int, r: int) -> str:
    adjs = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    for _ in range(m):
        v1,v2 = map(int, input().split())
        adjs[v1].append(v2)
        adjs[v2].append(v1)
    for adj in adjs[1:]:
        adj.sort()

    order = 1
    stack = [r]
    while stack:
        p_v = stack.pop()
        if visited[p_v]:
            continue
        visited[p_v] = order
        order += 1

        for c_v in adjs[p_v]:
            if not visited[c_v]:
                stack.append(c_v)

    return '\n'.join(map(str, visited[1:]))


print(sol(*map(int, input().split())))
