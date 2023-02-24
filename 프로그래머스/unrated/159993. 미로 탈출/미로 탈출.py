def solution(maps):
    class Found(Exception): pass


    def adjs(row, col):
        if row:  yield row-1, col
        if col:  yield row, col-1
        if row < N-1:  yield row+1, col
        if col < M-1:  yield row, col+1


    N, M = len(maps), len(maps[0])
    try:
        for r in range(N):
            for c in range(M):
                if maps[r][c] == 'S':
                    raise Found
    except Found:
        que = [(r, c)]

    is_visited = [[False]*M for _ in range(N)]
    is_visited[r][c] = True
    dist = 0
    try:
        while que:
            tmp = []; dist += 1
            for r, c in que:
                for cr, cc in adjs(r, c):
                    if is_visited[cr][cc] or maps[cr][cc] == 'X':
                        continue
                    if maps[cr][cc] == 'L':
                        answer = dist
                        que = [(cr, cc)]
                        raise Found
                    is_visited[cr][cc] = True
                    tmp.append((cr, cc))
            que = tmp
        return -1
    
    except Found:
        is_visited = [[False]*M for _ in range(N)]
        is_visited[cr][cc] = True
        dist = 0
        while que:
            tmp = []; dist += 1
            for r, c in que:
                for cr, cc in adjs(r, c):
                    if is_visited[cr][cc] or maps[cr][cc] == 'X':
                        continue
                    if maps[cr][cc] == 'E':
                        return answer + dist
                    is_visited[cr][cc] = True
                    tmp.append((cr, cc))     
            que = tmp
        return -1
