from itertools import permutations as p
from copy import deepcopy


def solution(board, r, c):
    def bfs(r1, c1, r2, c2):
        v = [[False]*4 for _ in range(4)]
        v[r1][c1] = True
        q = [(r1, c1)]
        d = 0
        while q:
            tmp = []
            for r, c in q:
                if r == r2 and c == c2:
                    return d
                for i in range(4):
                    nr, nc = r+dr[i], c+dc[i]
                    if 0 <= nr < 4 and 0 <= nc < 4 and not v[nr][nc]:
                        tmp.append((nr, nc))
                        v[nr][nc] = True
                    while 0 <= nr < 4 and 0 <= nc < 4:
                        if cur[nr][nc]:
                            if not v[nr][nc]:
                                tmp.append((nr, nc))
                                v[nr][nc] = True
                            break
                        nr += dr[i]; nc += dc[i]
                    else:
                        nr -= dr[i]; nc -= dc[i]
                        if not v[nr][nc]:
                            tmp.append((nr, nc))
                            v[nr][nc] = True
            q = tmp
            d += 1
        return

    
    cats = max(max(b) for b in board) + 1
    coords = [[(-1, -1), (-1, -1)] for _ in range(cats)]
    coords[0] = [(r, c), (r, c)]
    for r in range(4):
        for c in range(4):
            if not board[r][c]:
                continue
            i = 0 if coords[board[r][c]][0] == (-1, -1) else 1
            coords[board[r][c]][i] = (r, c)

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    miny = 255
    for seq in p(range(1, cats)):
        cur = deepcopy(board)
        cnt1 = cnt2 = s = 0
        for e in seq:
            d12, d21 = bfs(*coords[e][0], *coords[e][1]), bfs(*coords[e][1], *coords[e][0])
            cnt1, cnt2 =\
            min( cnt1 + bfs(*coords[s][0], *coords[e][1]), cnt2 + bfs(*coords[s][1], *coords[e][1]) ) + d21,\
            min( cnt1 + bfs(*coords[s][0], *coords[e][0]), cnt2 + bfs(*coords[s][1], *coords[e][0]) ) + d12
            cur[coords[e][0][0]][coords[e][0][1]] = cur[coords[e][1][0]][coords[e][1][1]] = 0
            s = e
        miny = min(miny, cnt1, cnt2)
    return miny + 2*(cats-1)
