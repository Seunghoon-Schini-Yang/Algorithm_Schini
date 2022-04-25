import sys
input = sys.stdin.readline

def sol(n: int, m: int) -> str:
    def get_path(s: int, e: int) -> str:
        if path[s][e]:
            return get_path(s, path[s][e]) + get_path(path[s][e], e)
        return [str(s)]
    

    INF = sys.maxsize
    dist = [[INF] * (n+1) for _ in range(n+1)]
    path = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        dist[i][i] = 0
    for _ in range(m):
        a,b,c = map(int, input().split())
        if c < dist[a][b]:
            dist[a][b] = c
    
    for mid in range(1,n+1):
        for i in range(1,n+1):
            if i == mid or dist[i][mid] == INF:
                continue
            for j in range(1,n+1):
                if j == mid or j == i:
                    continue
                if dist[i][mid]+dist[mid][j] < dist[i][j]:
                    dist[i][j] = dist[i][mid]+dist[mid][j]
                    path[i][j] = mid
    
    ans = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j or dist[i][j]==sys.maxsize:
                ans[i][j] = '0'
            else:
                ans[i][j] = get_path(i,j) + [str(j)]

    # '\n'.join('0' if i==j or dist[i][j]==sys.maxsize else ' '.join(str(len(ans[i][j])) + ans[i][j]) for i in range(1,n+1) for j in range(1,n+1))
    return '\n'.join(('\n'.join(' '.join(map(lambda x: '0' if x==sys.maxsize else str(x), line[1:])) for line in dist[1:]),'\n'.join('0' if i==j or dist[i][j]==sys.maxsize else ' '.join([str(len(ans[i][j]))] + ans[i][j]) for i in range(1,n+1) for j in range(1,n+1))))


print(sol(int(input()), int(input())))
