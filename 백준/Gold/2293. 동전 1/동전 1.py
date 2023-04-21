import sys
input = sys.stdin.readline


def solution(n: int, k: int) -> int:
    dp = [0] * (k+1)
    dp[0] = 1
    for _ in range(n):
        coin = int(input())
        for i in range(coin, k+1):
            if not dp[i-coin]:
                continue
            dp[i] += dp[i-coin]
    return dp[k]


print(solution(*map(int, input().split())))