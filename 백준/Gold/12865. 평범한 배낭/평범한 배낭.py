import sys
input = sys.stdin.readline


def solution(info: map) -> int:
    n, w_limit = info
    # pairs = [tuple(map(int, input().split())) for _ in range(n)]
    dp = [0] * (w_limit + 1)

    for w, v in [map(int, input().split()) for _ in range(n)]:
        for i in range(w_limit, w - 1, -1):
            if dp[i - w] + v > dp[i]:
                dp[i] = dp[i - w] + v
    
    return dp[w_limit]


print(solution(map(int, input().split())))
