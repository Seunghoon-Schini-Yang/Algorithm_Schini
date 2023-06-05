import sys
input = sys.stdin.readline


def adjs_conds(r, c):
    if 0 < r:  yield r-1, c
    if r < N-1:  yield r+1, c
    if 0 < c:  yield r, c-1
    if c < M-1:  yield r, c+1
        

def adjs(r, c):
    yield r-1, c
    yield r+1, c
    yield r, c+1
    yield r, c-1


def update_board(cands):
    while cands:
        r, c = cands.pop()
        for rr, cc in adjs(r, c):
            if board[rr][cc]:
                continue
            board[rr][cc] = 2
            cands.append((rr, cc))

            
def find_chz_melts():
    cands = []
    for r in range(N):
        for c in range(M):
            if board[r][c] != 1:
                continue
            if 2 <= sum(1 for rr, cc in adjs(r, c) if board[rr][cc] == 2):
                cands.append((r, c))
    for r, c in cands:
        board[r][c] = 2
    return cands


if __name__ == '__main__':
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    board[0][0] = 2
    cands = [(0, 0)]
    while cands:
        r, c = cands.pop()
        for rr, cc in adjs_conds(r, c):
            if board[rr][cc]:
                continue
            board[rr][cc] = 2
            cands.append((rr, cc))
    
    cnt = 0
    while True:
        cands = find_chz_melts()
        if cands:
            cnt += 1
        else:
            break
        update_board(cands)
    print(cnt)
