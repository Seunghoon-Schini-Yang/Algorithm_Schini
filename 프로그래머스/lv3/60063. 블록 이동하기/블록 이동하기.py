def solution(board):
    n = len(board)
    rmemo = [[False]*n for _ in range(n)]
    for r in range(n):
        rmemo[r][0] = True
    cmemo = [[False]*n for _ in range(n)]
    cmemo[0] = [True]*n
        
    dist = 0
    q = [(0, 1, 0)]
    rmemo[0][1] = True
    while q:
        tmp = []
        for r, c, d in q:
            if r == c == n-1:
                return dist
            if not d:
                if not rmemo[r][c-1] and not board[r][c-2]:
                    rmemo[r][c-1] = True
                    tmp.append((r, c-1, d))
                if c < n-1 and not rmemo[r][c+1] and not board[r][c+1]:
                    rmemo[r][c+1] = True   
                    tmp.append((r, c+1, d))
                if 0 < r and not board[r-1][c] and not board[r-1][c-1]:
                    if not rmemo[r-1][c]:
                        rmemo[r-1][c] = True
                        tmp.append((r-1, c, d))
                    if not cmemo[r][c]:
                        cmemo[r][c] = True
                        tmp.append((r, c, d^1))
                    if not cmemo[r][c-1]:
                        cmemo[r][c-1] = True
                        tmp.append((r, c-1, d^1))
                if r < n-1 and not board[r+1][c] and not board[r+1][c-1]:
                    if not rmemo[r+1][c]:
                        rmemo[r+1][c] = True
                        tmp.append((r+1, c, d))
                    if not cmemo[r+1][c]:
                        cmemo[r+1][c] = True
                        tmp.append((r+1, c, d^1))
                    if not cmemo[r+1][c-1]:
                        cmemo[r+1][c-1] = True
                        tmp.append((r+1, c-1, d^1))
            else:
                if not cmemo[r-1][c] and not board[r-2][c]:
                    cmemo[r-1][c] = True
                    tmp.append((r-1, c, d))
                if r < n-1 and not cmemo[r+1][c] and not board[r+1][c]:
                    cmemo[r+1][c] = True   
                    tmp.append((r+1, c, d))
                if 0 < c and not board[r][c-1] and not board[r-1][c-1]:
                    if not cmemo[r][c-1]:
                        cmemo[r][c-1] = True
                        tmp.append((r, c-1, d))
                    if not rmemo[r][c]:
                        rmemo[r][c] = True
                        tmp.append((r, c, d^1))
                    if not rmemo[r-1][c]:
                        rmemo[r-1][c] = True
                        tmp.append((r-1, c, d^1))
                if c < n-1 and not board[r][c+1] and not board[r-1][c+1]:
                    if not cmemo[r][c+1]:
                        cmemo[r][c+1] = True
                        tmp.append((r, c+1, d))
                    if not rmemo[r][c+1]:
                        rmemo[r][c+1] = True
                        tmp.append((r, c+1, d^1))
                    if not rmemo[r-1][c+1]:
                        rmemo[r-1][c+1] = True
                        tmp.append((r-1, c+1, d^1))      
        dist += 1
        q = tmp
