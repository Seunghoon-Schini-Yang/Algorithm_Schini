def solution(n: int, money: list):
    memo = [0]*(n+1)
    memo[0] = 1
    money.sort()

    for coin in money:
        for i in range(coin, n+1):
            memo[i] += memo[i-coin]

    return memo[-1]
    