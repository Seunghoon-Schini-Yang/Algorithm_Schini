import sys
input = sys.stdin.readline


def sol(n: int, p1: int, p2: int, m: int) -> int:
    def dfs(p: int, dgr: int) -> int:
        if p == p2:
            return dgr
        
        for c in graph[p]:
            if not visited[c]:
                visited[c] = True
                cnt = dfs(c, dgr+1)
                if cnt:
                    return cnt
        return 0
    

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False]*(n+1)
    visited[p1] = True
    ans = dfs(p1, 0)
    return ans if ans else -1


print(sol(int(input()), *map(int, input().split()), int(input())))
