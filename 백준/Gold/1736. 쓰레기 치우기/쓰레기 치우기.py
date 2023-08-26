import sys
input = sys.stdin.readline


class Board():
    def __init__(self, N, M):
        board = [list(map(int, input().split())) for _ in range(N)]
        board = [[j for j in range(M) if board[i][j]] for i in range(N)]
        cnt = 0
        for i in range(N):
            if not board[i]:
                continue
            cnt += 1
            cur = board[i][-1]
            for j in range(i+1, N):
                if not board[j] or board[j][-1] < cur:
                    continue
                tmp = board[j][-1]
                while board[j] and cur <= board[j][-1]:
                    board[j].pop()
                cur = tmp
        self.robots_count = cnt


if __name__ == '__main__':
    board = Board(*map(int, input().split()))
    print(board.robots_count)
