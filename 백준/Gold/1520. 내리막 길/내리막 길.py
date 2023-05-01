import sys
input = sys.stdin.readline
sys.setrecursionlimit(pow(10, 9))


def dfs(r, c):
    ways = 0
    for dr, dc in zip(dm, dn):
        if 0 <= (rr := r+dr) < M and 0 <= (cc := c+dc) < N and board[rr][cc] < board[r][c]:
            if memo[rr][cc] == -1:
                continue
            ways += memo[rr][cc] if memo[rr][cc] else dfs(rr, cc)
    memo[r][c] = ways if ways else -1
    return ways


if __name__ == '__main__':
    M, N = map(int, input().split())
    if M == N == 1:
        print(1)
    else:
        board = [list(map(int, input().split())) for _ in range(M)]
        memo = [[0] * N for _ in range(M)]
        memo[M-1][N-1] = 1
        dm = [0, 1, 0, -1]
        dn = [1, 0, -1, 0]
        print(dfs(0, 0))
