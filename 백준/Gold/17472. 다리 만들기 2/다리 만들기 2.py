import sys
input = sys.stdin.readline


def sol(n: int, m: int) -> int:
    def find(v: int) -> int:
        if rs[v] < 0:
            return v
        rs[v] = find(rs[v])
        return rs[v]


    def union(w: int, v1: int, v2: int) -> int:
        r1,r2 = find(v1),find(v2)
        if r1 == r2:
            return 0

        if rs[r1] < rs[r2]:
            rs[r2] = r1
        else:
            if rs[r1] == rs[r2]:
                rs[r2] -= 1
            rs[r1] = r2
        return w


    def dfs(i: int, j: int) -> None:
        stack = [(i,j)]
        visited[i][j] = 1
        while stack:
            x,y = stack.pop()
            locs[x][y] = land_cnt
            for cx,cy in zip((x+1,x-1,x,x), (y,y,y+1,y-1)):
                if 0 <= cx < n and 0 <= cy < m:
                    if not locs[cx][cy] or visited[cx][cy]:
                        continue
                    stack.append((cx,cy))
                    visited[cx][cy] = 1


    def get_edge(i: int, j: int) -> None:
        p_land = locs[i][j]
        if j < m-3:
            hz = j+1
            while hz < m and not locs[i][hz]:
                hz += 1
            if j+2 < hz < m and locs[i][hz] != p_land:
                c_land = locs[i][hz]
                w = hz-j-1
                if w < edges[p_land][c_land]:
                    edges[p_land][c_land] = w
                    edges[c_land][p_land] = w
        if i < n-3:
            vt = i+1
            while vt < n and not locs[vt][j]:
                vt += 1
            if i+2 < vt < n and locs[vt][j] != p_land:
                c_land = locs[vt][j]
                w = vt-i-1
                if w < edges[p_land][c_land]:
                    edges[p_land][c_land] = w
                    edges[c_land][p_land] = w
    

    locs = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    land_cnt = 1
    for i in range(n):
        for j in range(m):
            if not locs[i][j] or visited[i][j]:
                continue
            dfs(i, j)
            land_cnt += 1

    edges = [[10] * land_cnt for _ in range(land_cnt)]
    for i in range(n):
        for j in range(m):
            if locs[i][j]:
                get_edge(i, j)

    edges_flat = []
    for i in range(2, land_cnt):
        for j in range(1, i):
            if edges[i][j] < 10:
                edges_flat.append((edges[i][j],i,j))
    edges_flat.sort()

    w_sum = 0
    rs = [-1] * land_cnt
    for w,v1,v2 in edges_flat:
        w_sum += union(w,v1,v2)

    n_cnt = 0
    for r in rs[1:]:
        if r < 0:
            n_cnt += 1
    if n_cnt > 1:
        return -1
    return w_sum


print(sol(*map(int, input().split())))
