import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque


def sol(n: int, m: int) -> None:
    graph = [[] for _ in range(n+1)]
    degree = [0]*(n+1)
    que = deque()

    for _ in range(m):
        f,b = map(int, input().split())
        graph[f].append(b)
        degree[b] += 1
    
    for i in range(1, n+1):
        if not degree[i]:
            que.append(i)
    
    while que:
        cur = que.popleft()
        print(f'{cur} ')
        for x in graph[cur]:
            degree[x] -= 1
            if not degree[x]:
                que.append(x)
    return


sol(*map(int, input().split()))
