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
        adj.sort(reverse=True)
    
    que = [r]
    visited[r] = 1
    order = 2

    while que:
        temp = list()
        
        for p_v in que:
            for c_v in adjs[p_v]:
                if not visited[c_v]:
                    visited[c_v] = order
                    order += 1
                    temp.append(c_v)

        que = temp

    return '\n'.join(map(str, visited[1:]))


print(sol(*map(int, input().split())))
