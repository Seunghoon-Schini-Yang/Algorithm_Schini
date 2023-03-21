def solution(board):
    N, M = len(board), len(board[0])
    start = (0, 0)
    for r in range(N):
        for c in range(M):
            if board[r][c] == 'R':
                start = (r, c)
    is_visited = [[False] * M for _ in range(N)]
    is_visited[start[0]][start[1]] = True
    dr = (0, 1, 0, -1)
    dc = (1, 0, -1, 0)
    cnt = 0

    que = [start]
    while que:
        cnt += 1
        tmp = []
        for r, c in que:
            for i in range(4):
                cr, cc = r, c
                while 0 <= cr+dr[i] < N and 0 <= cc+dc[i] < M and board[cr+dr[i]][cc+dc[i]] != 'D':
                    cr += dr[i]
                    cc += dc[i]
                if is_visited[cr][cc]:
                    continue
                if board[cr][cc] == 'G':
                    return cnt
                is_visited[cr][cc] = True
                tmp.append((cr, cc))
        que = tmp
    
    return -1
