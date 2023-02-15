import sys
input = sys.stdin.readline


def main():
    N, M, K = map(int, input().split())
    if K == 1:
        return 0
    
    board = [input().rstrip() for _ in range(N)]
    memo = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if (not (r+c)%2 and board[r][c] == 'B') or ((r+c)%2 and board[r][c] == 'W'):
                continue
            memo[r][c] = 1
    
    board = [[0]*(M-K+1) for _ in range(N)]
    for r in range(N):
        board[r][0] = sum(memo[r][:K])
    for r in range(N):
        for c in range(K, M):
            board[r][c-K+1] = board[r][c-K] + memo[r][c] - memo[r][c-K]
    
    memo = [[0]*(M-K+1) for _ in range(N-K+1)]
    for c in range(M-K+1):
        memo[0][c] = sum(board[r][c] for r in range(K))
    for c in range(M-K+1):
        for r in range(K, N):
            memo[r-K+1][c] = memo[r-K][c] + board[r][c] - board[r-K][c]
    
    maxy = miny = memo[0][0]
    for r in memo:
        for c in r:
            if c < miny:
                miny = c
            elif c > maxy:
                maxy = c
    return min(miny, K*K-maxy)


if __name__ == '__main__':
    print(main())
