import sys
input = sys.stdin.readline
from itertools import accumulate

def solution(n: int) -> int:
    files = [0] + list(map(int, input().split()))
    acc = list(accumulate(files))
    dp = [[0] * (n+1) for _ in range(n+1)]

    return partial_sum(1, n, acc, dp) - acc[n]


def partial_sum(s: int, e: int, acc: list, dp: list) -> int:
    if dp[s][e]:
        return dp[s][e]

    range_sum = acc[e] - acc[s-1]
    if s == e:
        dp[s][e] = range_sum
        return dp[s][e]

    dp[s][e] = range_sum + min(partial_sum(s, k, acc, dp) + partial_sum(k+1, e, acc, dp) for k in range(s, e))
    return dp[s][e]


print('\n'.join([str(solution(int(input()))) for _ in range(int(input()))]))