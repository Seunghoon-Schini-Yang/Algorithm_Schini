import sys
input = sys.stdin.readline


def main():
    prefs = {}
    board = [[0] * N for _ in range(N)]

    for _ in range(N**2):
        student, *pref = map(int, input().split())
        prefs[student] = pref
        mstd = memp = -1
        mr = mc = N

        for r in range(N):
            for c in range(N):
                if board[r][c]:
                    continue
                std = emp = 0
                for rr, cc in adjs(r, c):
                    if not board[rr][cc]:
                        emp += 1
                    elif board[rr][cc] in prefs[student]:
                        std += 1
                if std < mstd or (std == mstd and emp <= memp):
                    continue
                mstd, memp = std, emp
                mr, mc = r, c

        board[mr][mc] = student

    answer = 0
    table = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}
    for r in range(N):
        for c in range(N):
            answer += table[sum(1 if board[rr][cc] in prefs[board[r][c]] else 0 for rr, cc in adjs(r, c))]
    print(answer)


def adjs(r, c):
    if r > 0:  yield r-1, c
    if c > 0:  yield r, c-1
    if r < N-1:  yield r+1, c
    if c < N-1:  yield r, c+1


if __name__ == '__main__':
    N = int(input())
    main()
