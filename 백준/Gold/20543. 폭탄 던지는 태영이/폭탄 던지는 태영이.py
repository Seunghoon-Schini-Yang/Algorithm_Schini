import sys
input = sys.stdin.readline


class Inha():
    def __init__(self, N, M):
        board = [[0]*(N-M+1) for _ in range(M-1)] + [list(map(lambda x: -int(x), input().split()))[:(N-M+1)] for _ in range(N-M+1)]
        for c in range(N-M+1):
            acc = 0
            for r in range(M-1, N):
                board[r][c] -= acc
                acc += board[r][c] - board[r-M+1][c]
        board = board[M-1:]

        board = [[0]*(M-1) + row for row in board]
        for r in range(N-M+1):
            acc = 0
            for c in range(M-1, N):
                board[r][c] -= acc
                acc += board[r][c] - board[r][c-M+1]
        board = [row[M-1:] for row in board]
        board = [[0]*N for _ in range(M>>1)] + [[0]*(M>>1) + row + [0]*(M>>1) for row in board] + [[0]*N for _ in range(M>>1)]
        self.board = board


if __name__ == '__main__':
    uni = Inha(*map(int, input().split()))
    print('\n'.join(' '.join(map(str, row)) for row in uni.board))
