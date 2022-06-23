import sys
input = sys.stdin.readline


def adjs(r: int, c: int) -> tuple:
    yield r, c+1
    yield r+1, c
    yield r, c-1
    yield r-1, c


def backtrack(r: int, c: int, depth: int) -> int:
    if depth == 3:
        return board[r][c]
    
    if depth == 1:
        for nr, nc in adjs(r, c):
            if 0<=nr<n and 0<=nc<m and not visited[nr][nc]:
                pass

    maxy = 0
    cnt = list()
    for nr, nc in adjs(r, c):
        if 0<=nr<n and 0<=nc<m and not visited[nr][nc]:
            cnt.append(board[nr][nc])
            visited[nr][nc] = True
            maxy = max(maxy, backtrack(nr, nc, depth+1))
            visited[nr][nc] = False

    if not depth and len(cnt) == 2:
        maxy = max((maxy, board[r+1][c]+backtrack(r, c+1, depth+2), board[r][c+1]+backtrack(r+1, c, depth+2)))

    if depth == 1:
        if len(cnt) == 2:
            maxy = max(maxy, sum(cnt))
        elif len(cnt) == 3:
            maxy = max(maxy, sum(cnt)-min(cnt))
    
    return board[r][c] + maxy


if __name__ == '__main__':
    n,m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False]*m for _ in range(n)]

    ans = 0
    for r in range(n):
        for c in range(m):
            visited[r][c] = True
            ans = max(ans, backtrack(r, c, 0))
            board[r][c]
    
    print(ans)
