# bfs
import sys
input = sys.stdin.readline
from collections import deque

def sol(n: int) -> str:
    parents = [0] * (n+1)
    parents[1] = 1

    tree = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    q = deque([1])
    while q:
        for _ in range(len(q)):
            p_n = q.popleft()
            for c_n in tree[p_n]:
                if not parents[c_n]:
                    parents[c_n] = p_n
                    q.append(c_n)

    return '\n'.join(map(str, parents[2:]))


print(sol(int(input())))
