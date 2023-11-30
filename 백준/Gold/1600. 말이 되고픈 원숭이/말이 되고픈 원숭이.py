import sys
input = sys.stdin.readline


def main():
    k = int(input())
    W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    memo = [[k+1] * W for _ in range(H)]


    def move_horse(r, c):
        if r > 0:
            if c > 1:  yield r-1, c-2
            if c < W-2:  yield r-1, c+2
        if r > 1:
            if c > 0:  yield r-2, c-1
            if c < W-1:  yield r-2, c+1
        if r < H-1:
            if c > 1:  yield r+1, c-2
            if c < W-2:  yield r+1, c+2
        if r < H-2:
            if c > 0:  yield r+2, c-1
            if c < W-1:  yield r+2, c+1

    def move_adj(r, c):
        if r > 0:  yield r-1, c
        if r < H-1:  yield r+1, c
        if c > 0:  yield r, c-1
        if c < W-1:  yield r, c+1

    def bfs_round(q):
        tmp = []
        for cnt, (r, c) in q:
            if cnt < k:
                for nr, nc in move_horse(r, c):
                    if board[nr][nc] or memo[nr][nc] <= cnt+1:
                        continue
                    if nr == H-1 and nc == W-1:
                        return tmp, True
                    memo[nr][nc] = cnt+1
                    tmp.append((cnt+1, (nr, nc)))
            for nr, nc in move_adj(r, c):
                if board[nr][nc] or memo[nr][nc] <= cnt:
                    continue
                if nr == H-1 and nc == W-1:
                    return tmp, True
                memo[nr][nc] = cnt
                tmp.append((cnt, (nr, nc)))
        return tmp, False
    

    if W == H == 1:
        print(0)
    elif board[-1][-1]:
        print(-1)
    else:
        q = [(0, (0, 0))]
        rnd = 1
        while q:
            q, is_arrived = bfs_round(q)
            if is_arrived:  break
            rnd += 1
        print(rnd if is_arrived else -1)


if __name__ == '__main__':
    main()
