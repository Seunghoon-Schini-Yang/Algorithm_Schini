def solution(n):
    memo = [0] * (n+1)
    memo[0] = memo[1] = 1
    for i in range(2, n+1):
        memo[i] = sum(memo[j] * memo[i-1-j] for j in range(i))
    return memo[n]
