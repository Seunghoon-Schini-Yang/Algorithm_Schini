# bfs
import sys
input = sys.stdin.readline


def adjs(row: int, col: int) -> tuple:
    yield row+1, col
    yield row-1, col
    yield row, col+1
    yield row, col-1


def bfs_start(row: int, col: int) -> tuple:
    global f

    if board[row][col] and board[row][col] != 1:
        return (row, col)
    
    burn = 1
    o_r = o_c = n
    visited = [[False]*n for _ in range(n)]
    visited[row][col] = True
    que = [(row, col)]

    while que:
        temp = list()
        for _ in range(len(que)):
            for nr, nc in adjs(*que.pop()):
                if 0<=nr<n and 0<=nc<n:
                    if board[nr][nc] == 1:
                        continue
                    if not visited[nr][nc]:
                        visited[nr][nc] = True                        
                        if not board[nr][nc]:
                            temp.append((nr, nc))
                        else:
                            if nr < o_r or (nr == o_r and nc < o_c):
                                o_r = nr; o_c = nc
        if o_r != n:
            f -= burn
            return (o_r, o_c)
        burn += 1
        que = temp

    return (n, n)


def bfs_end(s_r: int, s_c: int, e_r: int, e_c: int) -> tuple:
    global f
    
    burn = 1
    visited = [[False]*n for _ in range(n)]
    visited[s_r][s_c] = True
    que = [(s_r, s_c)]

    while que:
        temp = list()
        for _ in range(len(que)):
            for nr, nc in adjs(*que.pop()):
                if 0<=nr<n and 0<=nc<n and board[nr][nc] != 1 and not visited[nr][nc]:
                    if nr == e_r and nc == e_c:
                        f -= burn
                        if f >= 0:
                            f += burn<<1
                        return (e_r, e_c)
                    visited[nr][nc] = True
                    temp.append((nr, nc))
        burn += 1
        que = temp
    
    return (n, n)


if __name__ == '__main__':
    n,m,f = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    c_r, c_c = map(lambda x: int(x)-1, input().split())
    for _ in range(m):
        s_r, s_c, e_r, e_c = map(lambda x: int(x)-1, input().split())
        board[s_r][s_c] = (e_r, e_c)

    is_break = False
    for _ in range(m):
        c_r, c_c = bfs_start(c_r, c_c)
        if c_r == n or f <= 0:
            is_break = True
            print(-1)
            break

        e_r, e_c = board[c_r][c_c]
        board[c_r][c_c] = 0
        c_r, c_c = bfs_end(c_r, c_c, e_r, e_c)
        if c_r == n or f < 0:
            is_break = True
            print(-1)
            break
    
    if not is_break:
        print(f)
