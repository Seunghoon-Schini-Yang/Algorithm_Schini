# implementation (빡구현) + bfs
import sys
input = sys.stdin.readline


def sol(n: int, m: int) -> int:
    cnt = 0
    visited = set()
    board = [list(input().rstrip()) for _ in range(n)]
    for row in range(1, n-1):
        for col in range(1, m-1):
            if board[row][col] == 'R':
                r_r = row; r_c = col
                board[row][col] = '.'
            elif board[row][col] == 'B':
                b_r = row; b_c = col
                board[row][col] = '.'

    # left, right, up, down
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    
    visited.add((r_r,r_c,b_r,b_c))
    que = [(r_r,r_c,b_r,b_c)]

    while que:
        cnt += 1
        if cnt > 10:
            return -1
        
        temp = list()
        for _ in range(len(que)):
            r_r,r_c,b_r,b_c = que.pop()

            for i in range(4):
                trr = tbr = trc = tbc = 0
                r_arrived = b_arrived = False

                while True:
                    if board[r_r+trr+dr[i]][r_c+trc+dc[i]] == '#':
                        break
                    elif board[r_r+trr+dr[i]][r_c+trc+dc[i]] == 'O':
                        r_arrived = True
                        break
                    trr += dr[i]; trc += dc[i]
                while True:
                    if board[b_r+tbr+dr[i]][b_c+tbc+dc[i]] == '#':
                        break
                    elif board[b_r+tbr+dr[i]][b_c+tbc+dc[i]] == 'O':
                        b_arrived = True
                        break
                    tbr += dr[i]; tbc += dc[i]
                
                if b_arrived:
                    continue
                if r_arrived:
                    return cnt
                
                if r_r+trr == b_r+tbr and r_c+trc == b_c+tbc:
                    if abs(trr)-abs(tbr) > 0:
                        trr -= dr[i]
                    else:
                        tbr -= dr[i]
                    if abs(trc)-abs(tbc) > 0:
                        trc -= dc[i]
                    else:
                        tbc -= dc[i]
                
                if (r_r+trr,r_c+trc,b_r+tbr,b_c+tbc) not in visited:
                    visited.add((r_r+trr,r_c+trc,b_r+tbr,b_c+tbc))
                    temp.append((r_r+trr,r_c+trc,b_r+tbr,b_c+tbc))

        que = temp
    
    return -1


print(sol(*map(int, input().split())))
