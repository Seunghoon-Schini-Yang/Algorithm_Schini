import sys
input = sys.stdin.readline


def sol(n: int) -> int:
    def dfs(k: int, mask: int) -> int:
        if k == n:
            return 0
        
        if dp[mask] < INF:
            return dp[mask]
        
        for i in range(n):
            if not mask & (1 << i):
                dp[mask] = min(dp[mask], dfs(k+1, mask | (1 << i)) + w[k][i])

        return dp[mask]


    INF = sys.maxsize
    w = [list(map(int, input().split())) for _ in range(n)]
    dp = [INF for _ in range(1 << n)]

    return dfs(0,0)


print(sol(int(input())))
