import sys
INF = sys.maxsize

def solution(board):
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    n = len(board)
    memo = [[[INF]*4 for _ in range(n)] for _ in range(n)]
    memo[0][0][0] = memo[0][0][2] = 0
    q = [(0, 0, 0, 0), (0, 0, 0, 2)]
    while q:
        tmp = []
        for r, c, cost, d in q:
            nr, nc = r+dr[d], c+dc[d]
            ncost = cost+100
            if 0 <= nr < n and 0 <= nc < n and not board[nr][nc] and ncost < memo[nr][nc][d]:
                memo[nr][nc][d] = ncost
                tmp.append((nr, nc, ncost, d))
            for i in range(4):
                if i==d:
                    continue
                nr, nc = r+dr[i], c+dc[i]
                ncost = cost + 600
                if 0 <= nr < n and 0 <= nc < n and not board[nr][nc]  and ncost < memo[nr][nc][i]:
                    memo[nr][nc][i] = ncost
                    tmp.append((nr, nc, ncost, i))
        q = tmp
    return min(memo[-1][-1])
