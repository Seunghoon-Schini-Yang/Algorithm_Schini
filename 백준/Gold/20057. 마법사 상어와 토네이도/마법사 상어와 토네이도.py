import sys
input = sys.stdin.readline


def scatter(d, r, c):
    dr, dc = drr[d], dcc[d]
    sand = board[r][c]
    update(r+(2*dr), c+(2*dc), board[r][c]//20)
    update(r+dr+dc, c+dc+dr, board[r][c]//10)
    update(r+dr-dc, c+dc-dr, board[r][c]//10)
    update(r+(2*dc), c+(2*dr), board[r][c]//50)
    update(r-(2*dc), c-(2*dr), board[r][c]//50)
    update(r+dc, c+dr, board[r][c]*7//100)
    update(r-dc, c-dr, board[r][c]*7//100)
    update(r-dr+dc, c-dc+dr, board[r][c]//100)
    update(r-dr-dc, c-dc-dr, board[r][c]//100)
    sand -= sand//20 + (sand//10 + sand//50 + sand//100 + sand*7//100)*2
    update(r+dr, c+dc, sand)
    board[r][c] = 0
    return


def update(r, c, amount):
    global out
    if 0 <= r < N and 0 <= c < N:
        board[r][c] += amount
    else:
        out += amount
    
        
if __name__ == '__main__':
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    out = d = 0
    r = c = N>>1
    drr = [0, 1, 0, -1]
    dcc = [-1, 0, 1, 0]
    for i in range(1, N):
        for _ in range(2):
            for _ in range(i):
                r += drr[d]
                c += dcc[d]
                scatter(d, r, c)
            d = (d+1)%4
    for _ in range(N-1):
        r += drr[d]
        c += dcc[d]
        scatter(d, r, c)
    print(out)
