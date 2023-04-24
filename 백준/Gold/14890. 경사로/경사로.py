import sys
input = sys.stdin.readline


def calc_row(row):
    cur = row[0]
    acc = L
    for h in row:
        if cur == h:
            acc += 1
        elif cur+1 == h:
            if acc < L2:
                return 0
            acc = L+1
        elif cur == h+1:
            if acc < L:
                return 0
            acc = 1
        else:
            return 0
        cur = h
    return 0 if acc < L else 1


if __name__ == '__main__':
    N, L = map(int, input().split())
    L2 = L<<1
    board = [list(map(int, input().split())) for _ in range(N)]
    cnt = sum(calc_row(row) for row in board)
    cnt += sum(calc_row(list(row)) for row in zip(*board))
    print(cnt)
    