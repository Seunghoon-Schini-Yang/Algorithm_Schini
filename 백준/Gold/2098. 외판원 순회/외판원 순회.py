import sys
input = sys.stdin.readline


def sol(n: int) -> int:
    def dfs(p_n: int, mask: int) -> int:
        if mask+2 == (1<<n):
            if w[p_n][0]:
                return w[p_n][0]
            else:
                return INF
        
        if memo[p_n][mask] < INF:
            return memo[p_n][mask]

        for i in range(1, n):
            if not mask & (1<<i) and w[p_n][i]:
                memo[p_n][mask] = min(memo[p_n][mask], dfs(i, mask|(1<<i)) + w[p_n][i])
        return memo[p_n][mask]

    
    INF = sys.maxsize
    w = [list(map(int, input().split())) for _ in range(n)]
    memo = [[INF] * (1 << n) for _ in range(n)]

    return dfs(0, 0)


print(sol(int(input())))
