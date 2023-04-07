import sys
input = sys.stdin.readline


def main() -> int:
    board = [input().rstrip() for _ in range(N)]
    kemo = [[K+1] * M for _ in range(N)]
    kemo[0][0] = cnt = 0

    que = [(0, 0, 0)]
    while que:
        cnt += 1
        tmp = []
        for r, c, k in que:
            if (r, c) == (N-1, M-1):
                return cnt
            for rr, cc in adjs(r, c):
                kk = k
                if board[rr][cc] == '1':
                    kk += 1
                if K < kk or kemo[rr][cc] <= kk:
                    continue
                kemo[rr][cc] = kk
                tmp.append((rr, cc, kk))
        que = tmp
    return -1


def adjs(r, c):
    if 0 < r:  yield (r-1, c)
    if r < N-1:  yield (r+1, c)
    if 0 < c:  yield (r, c-1)
    if c < M-1:  yield (r, c+1)


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    cnt = main()
    print(cnt)
