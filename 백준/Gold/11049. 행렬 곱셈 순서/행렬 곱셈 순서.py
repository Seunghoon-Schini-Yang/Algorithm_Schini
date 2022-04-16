import sys
input = sys.stdin.readline

def solution(n: int) -> int:
    h = [0] * n
    w = [0] * n
    for i in range(n):
        h[i], w[i] = map(int, input().split())

    dp = [[0] * n for _ in range(n)]
    for step in range(1, n):
        for r in range(n-step):
            m = r + step
            dp[r][m] = min(h[r]*w[k]*w[m] + dp[r][k] + dp[k+1][m] for k in range(r, m))

    return dp[0][n-1]


print(solution(int(input())))
