# bfs
import sys
input = sys.stdin.readline


def get_origin() -> tuple:
    for r in range(n):
        for c in range(n):
            if sea[r][c] == 9:
                return r, c


def bfs(row: int, col: int) -> tuple:
    cdist = 1
    visited = [[False]*n for _ in range(n)]
    visited[row][col] = True

    que = [(row, col)]
    while que:
        temp = list()
        candidate = list()
        for _ in range(len(que)):
            row, col = que.pop()
            for cr, cc in adjs(row, col):
                if 0<=cr<n and 0<=cc<n and not visited[cr][cc] and sea[cr][cc] <= size:
                    visited[cr][cc] = True
                    if not sea[cr][cc] or sea[cr][cc] == size:
                        temp.append((cr, cc))
                    else:
                        candidate.append((cr, cc))
        
        if candidate:
            sr, sc = min(candidate)
            sea[sr][sc] = 0
            return cdist, sr, sc
        
        que = temp
        cdist += 1
    return 0, 0, 0


def adjs(row: int, col: int) -> tuple:
    yield row-1, col
    yield row, col-1
    yield row, col+1
    yield row+1, col


if __name__ == '__main__':
    n = int(input())
    sea = [list(map(int, input().split())) for _ in range(n)]
    dist = 0
    size = 2; eat = 0
    
    sr, sc = get_origin()
    sea[sr][sc] = 0

    while True:
        cdist, sr, sc = bfs(sr, sc)
        if not cdist:
            break
        dist += cdist

        eat += 1
        if eat == size:
            size += 1
            eat = 0

    print(dist)
