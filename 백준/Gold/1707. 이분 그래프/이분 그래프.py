import sys
input = sys.stdin.readline
from collections import deque

def sol(n: int) -> str:
    return '\n'.join(is_bipartite(*map(int, input().split())) for _ in range(n))


def is_bipartite(v: int, e: int) -> str:
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    is_odd = False
    v1, v2 = [0]*(v+1), [0]*(v+1)
    to_visit = set(range(1, v+1))
    q = deque()

    while to_visit:
        add_q = to_visit.pop()
        q.append(add_q)
        if not is_odd:
            v1[add_q] = 1
        else:
            v2[add_q] = 1
        
        while q:
            for _ in range(len(q)):
                vertex = q.popleft()
                for node in graph[vertex]:
                    if is_odd:
                        if v2[node]:
                            return 'NO'
                        elif not v1[node]:
                            v1[node] = 1
                            to_visit.remove(node)
                            q.append(node)
                    else:
                        if v1[node]:
                            return 'NO'
                        elif not v2[node]:
                            v2[node] = 1
                            to_visit.remove(node)
                            q.append(node)
            is_odd = not is_odd
    return 'YES'


print(sol(int(input())))
