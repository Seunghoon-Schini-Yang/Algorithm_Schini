def solution(n: int, money: list):
    money.sort()
    m_n = len(money)
    memo = [[0]*(n+1) for _ in range(m_n)]
    for ci in range(m_n):
        memo[ci][0] = 1

    for i in range(money[0], n+1):
        memo[0][i] = memo[0][i-money[0]]
        for ci in range(1, m_n):
            memo[ci][i] = memo[ci-1][i] + (0 if i < money[ci] else memo[ci][i-money[ci]])

    return memo[-1][-1]
    